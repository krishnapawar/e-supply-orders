from fastapi import HTTPException

from app.models.category import Category
from app.repositories.category import CategoryRepository


class CategoryService:

    @staticmethod
    def create(db, data):

        category = Category(**data.model_dump())

        return CategoryRepository.create(db, category)

    @staticmethod
    def get_all(db, params):

        return CategoryRepository.get_all(db, params)

    @staticmethod
    def get_by_id(db, id):

        category = CategoryRepository.get_by_id(db, id)

        if not category:
            raise HTTPException(404, "Category not found")

        return category

    @staticmethod
    def update(db, id, data):

        category = CategoryRepository.get_by_id(db, id)

        if not category:
            raise HTTPException(404, "Category not found")

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(category, key, value)

        return CategoryRepository.update(db, category)

    @staticmethod
    def delete(db, id):

        category = CategoryRepository.get_by_id(db, id)

        if not category:
            raise HTTPException(404, "Category not found")

        CategoryRepository.delete(db, category)

        return {
            "message": "Category deleted successfully"
        }