from fastapi import FastAPI
from importlib import import_module
from api.core.config import settings

TAGS_METADATA: list[dict] = [  # for better documentation in openapi spec
    {
        "name": "Health",
        "description": "Public endpoints for checking health of api server",
    },
    {
        "name": "Doc",
        "description": "holds info about the Doc entries and helps to manage their positions"
    },
]


def route_setup(app: FastAPI):
    """
    This method is used to set all the routers to the ASGI app
    To add new routes to the application,
    Add your file name (Capitalised without extension) in the TAGS_METADATA list
    """
    print("Setting up the routes ...")
    for tags in TAGS_METADATA:
        tag_name: str = tags["name"]
        module = import_module(f".{tag_name.lower()}", "api.routes")
        route = getattr(module, f"{tag_name.lower()}_router")
        app.include_router(route, tags=[tag_name],  prefix=settings.API_V1_STR)
