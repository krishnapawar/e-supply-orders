from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.permissions import require_role
from app.database.dependencies import get_db
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)
from app.services.product import ProductService
from app.core.pagination import pagination_params
from app.schemas.pagination import PaginationParams

router = APIRouter()


@router.post(
    "",
    response_model=ProductResponse,
    status_code=201
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return ProductService.create_product(db, product)


# @router.get(
#     "",
#     response_model=list[ProductResponse]
# )
# def get_products(
#     db: Session = Depends(get_db)
# ):
#     return ProductService.get_products(db)

@router.get("")
def get_products(
    params: PaginationParams = Depends(pagination_params),
    db: Session = Depends(get_db)
):
    print("parms==>",params)
    return ProductService.get_products(
        db,
        params
    )


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return ProductService.get_product(db, product_id)


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    return ProductService.update_product(db, product_id, product)


@router.delete(
    "/{product_id}"
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return ProductService.delete_product(db, product_id)