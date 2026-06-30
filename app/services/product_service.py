from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repository import ProductRepository


class ProductService:

    @staticmethod
    def create_product(db: Session, data):

        product = Product(**data.model_dump())

        return ProductRepository.create(db, product)

    @staticmethod
    def get_products(db: Session):

        return ProductRepository.get_all(db)

    @staticmethod
    def get_product(db: Session, product_id: int):

        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product

    @staticmethod
    def update_product(db: Session, product_id: int, data):

        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        update_data = data.model_dump()

        for key, value in update_data.items():
            setattr(product, key, value)

        return ProductRepository.update(db, product)

    @staticmethod
    def delete_product(db: Session, product_id: int):

        product = ProductRepository.get_by_id(db, product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        ProductRepository.delete(db, product)

        return {
            "message": "Product deleted successfully"
        }