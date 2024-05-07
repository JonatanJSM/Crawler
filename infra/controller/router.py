from fastapi import APIRouter
from infra.controller.endpoints import cores
from infra.controller.endpoints import pages

api_router = APIRouter()


api_router.include_router(cores.router, tags=["cores"])
api_router.include_router(pages.router, tags=["pages"])
