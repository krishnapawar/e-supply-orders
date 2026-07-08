from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse


PUBLIC_PATHS = (
    "/docs",
    "/redoc",
    "/openapi.json",
    "/auth",
)

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith(PUBLIC_PATHS):
            return await call_next(request)

        token = request.headers.get("Authorization")

        if not token:
            return JSONResponse(
                status_code=401,
                content={"detail": "Missing Authorization header"},
            )

        # Validate token

        return await call_next(request)