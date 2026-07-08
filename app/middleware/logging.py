from fastapi import Request


async def logging_middleware(request: Request, call_next):

    print("=" * 60)
    print(f"METHOD : {request.method}")
    print(f"PATH   : {request.url.path}")
    print(f"CLIENT : {request.client.host}")

    response = await call_next(request)

    print(f"STATUS : {response.status_code}")
    print("=" * 60)

    return response