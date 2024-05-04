from fastapi import FastAPI, HTTPException, status
from models.page import Page
from models.core import Core
from crawler.engine import Engine
import searcher.tokenizer as tokenizer
import searcher.expander as expander
from solr.solrManager import SolrManager


app = FastAPI()


LANGUAGES_PATH = "json/languages.json"
solr_manager = SolrManager()


@app.post("/pages", summary="Probar por mientras con https://www.wagslane.dev")
def create_page(page: Page):
    urls = page.url
    engine = Engine(urls, 1, "prueba6")
    result = engine.start()
    if result:
        return {"message": "La página se guardó exitosamente", "page": urls}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Hubo un error al crear la página")


@app.post("/cores")
def create_core(core: Core):
    core_name = core.corename
    status_code = check_core(core_name)
    if status_code == 200:
        return {"message": f"El core {core_name} se creó exitosamente"}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Hubo un error al crear el core")


@app.get("/tokens")
def create_tokens(input):
    return tokenizer.tokenize_input(input, LANGUAGES_PATH)


@app.get("/synonyms")
def create_synonymsArray(word, language):
    return expander.get_similar_matrix(word, language)


def check_core(core_name):
    status_code = solr_manager.get_core_status(core_name)
    if status_code != 200:
        response = solr_manager.create_core(core_name, core_name)
        status_code = response.status_code
    return status_code
