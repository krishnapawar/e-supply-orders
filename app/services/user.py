from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.core.security import hash_password

from app.core.security import (
    verify_password,
    create_access_token
)


class UserService:

    @staticmethod
    def register(
        db: Session,
        user: UserCreate
    ):

        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        db_user = User(
            name=user.name,
            email=user.email,
            phone=user.phone,
            password=hash_password(user.password)
        )

        return UserRepository.create(
            db,
            db_user
        )
 

    @staticmethod
    def login(db: Session, data):

        user = UserRepository.get_by_email(
            db,
            data.email
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(
            data.password,
            user.password
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        token = create_access_token(
            {"sub": str(user.id)}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }