from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)


class ProductUpdate(BaseModel):
    name: str
    price: float
    stock: int


class ProductResponse(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }