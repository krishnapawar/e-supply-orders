from fastapi import Query

from app.schemas.pagination import PaginationParams


def pagination_params(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    sort: str = "id",
    order: str = "asc",
):
    return PaginationParams(
        page=page,
        limit=limit,
        search=search,
        sort=sort,
        order=order,
    )