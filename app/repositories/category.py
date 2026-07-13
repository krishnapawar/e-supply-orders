from app.models.category import Category
from app.repositories.base import BaseRepository


class CategoryRepository(BaseRepository):
    model = Category