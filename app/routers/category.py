from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.category import *

from app.services.category import CategoryService

from app.schemas.pagination import PaginationParams
from app.core.pagination import pagination_params

router = APIRouter()

@router.post(
    "",
    response_model=CategoryResponse,
    status_code=201
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return CategoryService.create(db, category)

@router.get("")
def get_categories(
    params: PaginationParams = Depends(pagination_params),
    db: Session = Depends(get_db)
):
    return CategoryService.get_all(
        db,
        params
    )

@router.get(
    "/{id}",
    response_model=CategoryResponse
)
def get_category(
    id: int,
    db: Session = Depends(get_db)
):
    return CategoryService.get_by_id(db, id)

@router.put(
    "/{id}",
    response_model=CategoryResponse
)
def update_category(
    id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db)
):
    return CategoryService.update(
        db,
        id,
        category
    )

@router.delete("/{id}")
def delete_category(
    id: int,
    db: Session = Depends(get_db)
):
    return CategoryService.delete(db, id)