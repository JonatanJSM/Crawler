from fastapi import APIRouter, HTTPException, status
from infra.dtos.core import Core
from infra.gateway.solr.solrManager import SolrManager

router = APIRouter()
solr_manager = SolrManager()


@router.post("/cores")
async def create_core(core: Core):
    core_name = core.corename
    status_code = check_core(core_name)
    if status_code == 200:
        return {"message": f"El core {core_name} se creó exitosamente"}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Hubo un error al crear el core")


def check_core(core_name):
    status_code = solr_manager.get_core_status(core_name)
    if status_code != 200:
        response = solr_manager.create_core(core_name, core_name)
        status_code = response.status_code
    return status_code
