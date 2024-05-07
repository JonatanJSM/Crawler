from fastapi import APIRouter
from infra.controller.endpoints import cores
from infra.controller.endpoints import pages
from infra.controller.endpoints import synonyms
from infra.controller.endpoints import tokens


api_router = APIRouter()


api_router.include_router(cores.router, tags=["cores"])
api_router.include_router(pages.router, tags=["pages"])
api_router.include_router(synonyms.router, tags=["synonyms"])
api_router.include_router(tokens.router, tags=["tokens"])
