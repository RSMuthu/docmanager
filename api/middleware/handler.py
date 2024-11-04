import os
from typing import Callable
from fastapi.requests import Request
from api.utils.exceptions import HTTPError
from api.core.db import get_db


async def http_exception_handler(request: Request, exc: HTTPError):
    if hasattr(request.state, "db"):
        await request.state.db.rollback()
    if os.environ.get("RAISE_HTTP_EXCEPTION") == "true":
        # for testing purpose
        raise exc
    return exc.json_response


class HandlerMiddleware:
    """
    Middleware to handle the HTTP Errors
    """

    async def __call__(self, request: Request, call_next: Callable):
        try:
            request.state.db = await anext(get_db())
            resp = await call_next(request)
            await request.state.db.commit()
            return resp
        except HTTPError as err:
            return await http_exception_handler(request, err)
