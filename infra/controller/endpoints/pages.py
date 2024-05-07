from fastapi import APIRouter, HTTPException, status
from models.page import Page
from core.usecase.engine import Engine

router = APIRouter()


@router.post("/pages", summary="Probar por mientras con https://www.wagslane.dev")
async def create_page(page: Page):
    urls = page.url
    engine = Engine(urls, 0, "prueba6")
    result = engine.start()
    if result:
        return {"message": "La página se guardó exitosamente", "page": urls}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Hubo un error al crear la página")
