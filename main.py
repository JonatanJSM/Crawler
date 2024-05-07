from fastapi import FastAPI
from infra.controller.router import api_router


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app


app = get_application()
