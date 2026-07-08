from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService
from app.schemas.auth import (
    LoginRequest,
    LoginResponse
)
from app.core.auth import get_current_user


router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.register(
        db,
        user
    )

@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    return UserService.login(
        db,
        data
    )

@router.get(
        "/me",
        response_model=UserResponse,
        status_code=200
)
def get_profile(
    current_user = Depends(get_current_user)
):
    return current_user