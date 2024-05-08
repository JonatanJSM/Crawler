from fastapi import APIRouter, HTTPException, status
from infra.models.page import Page
from core.usecase.engine import Engine
from infra.solr.solrAdapter import SolrManagerAdapter

router = APIRouter()


@router.post("/pages", summary="Probar por mientras con https://www.wagslane.dev")
async def create_page(page: Page):
    urls = page.url
    engine = Engine(urls, 0, "prueba6", solrClientManager=SolrManagerAdapter())
    result = engine.start()
    if result:
        return {"message": "La página se guardó exitosamente", "page": urls}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Hubo un error al crear la página")
