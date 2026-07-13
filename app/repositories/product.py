# from sqlalchemy.orm import Session
from app.models.product import Product
from app.repositories.base import BaseRepository


class ProductRepository(BaseRepository):
    model = Product
    # def __init__(self):
    #     super().__init__(Product)