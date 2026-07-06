from fastapi import FastAPI
from app.routers.product import router as product_router
from app.routers.auth import router as auth_router

from app.database.database import engine
from app.database.base import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ecommerce API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Ecommerce API"
    }

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    product_router,
    prefix="/products",
    tags=["Products"]
)