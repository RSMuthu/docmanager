from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.core.db import initiate as init_db
from api.middleware import custom_middleware_setup
from api.routes import TAGS_METADATA, route_setup


async def lifespan(app: FastAPI):
    # On startup
    # TODO: Change print to logger
    route_setup(app)
    print("Route Setup Done")
    await init_db()
    print("DB Loaded")
    yield
    # On Shutdown


def create_api() -> FastAPI:
    # description for the openapi doc is set in Markdown language
    # Add more description if needed
    description = """
## Docs Manager API

The API is intended to be used by web frontend application for displaying the docs added.
    """
    app: FastAPI = FastAPI(  # TODO: Fix the name later
        title="DOCMANAGER_API",
        description=description,
        openapi_tags=TAGS_METADATA,
        lifespan=lifespan,
    )

    custom_middleware_setup(app)

    # Add CORS Middleware to the application
    origins = [
        "*",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # # Mount the static files from the React build
    # app.mount("/static", StaticFiles(directory="client/build/static"), name="static")

    # # Set up templates directory where React's index.html resides
    # templates = Jinja2Templates(directory="client/build")

    # @app.get("/{rest_of_path:path}")
    # async def serve_spa(request: Request, rest_of_path: str):
    #     return templates.TemplateResponse("index.html", {"request": request})

    return app


app: FastAPI = create_api()
