from typing import Callable, List
from fastapi import FastAPI

from .handler import HandlerMiddleware


def custom_middleware_setup(app: FastAPI):
    """
    This method is used to set middleware to the app

    To add new middleware to the app,
    import the necessary custom middleware and
    add it to the `middleware_stack`.
    """
    middleware_stack: List[Callable] = [
        HandlerMiddleware(),
    ]

    for middleware in middleware_stack:
        app.middleware("http")(middleware)
