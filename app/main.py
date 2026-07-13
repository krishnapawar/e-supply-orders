from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.exceptions.handlers import (
    http_exception_handler,
    validation_exception_handler,
    global_exception_handler
)

from app.core.permissions import require_role
from app.routers.product import router as product_router
from app.routers.auth import router as auth_router
from app.routers.category import router as category_router

from app.database.database import engine
from app.database.base import Base
from app.middleware.timer import timer_middleware
from app.middleware.logging import logging_middleware
from app.middleware.request_body import request_body_middleware
from app.middleware.authentication import AuthenticationMiddleware
from app.middleware.cors import setup_cors

# Create tables
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ecommerce API",
    version="1.0.0"
)

setup_cors(app)

app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.middleware("http")(request_body_middleware)
app.middleware("http")(timer_middleware)
app.middleware("http")(logging_middleware)
# app.middleware("http")(AuthenticationMiddleware)
app.add_middleware(AuthenticationMiddleware)



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

@app.get("/dashboard")
def dashboard(
    current_user=Depends(require_role("admin"))
):
    return {
        "message": "Welcome Admin",
        "user": current_user.name
    }

app.include_router(
    product_router,
    prefix="/products",
    tags=["Products"]
)

app.include_router(
    category_router,
    prefix="/categories",
    tags=["Categories"]
)