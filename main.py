from fastapi import FastAPI
# import searcher.tokenizer as tokenizer
# import searcher.expander as expander
# from infra.solr.solrManager import SolrManager
from infra.controller.router import api_router

# LANGUAGES_PATH = "json/languages.json"


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app


app = get_application()

# @app.get("/tokens")
# def create_tokens(input):
#     return tokenizer.tokenize_input(input, LANGUAGES_PATH)

# @app.get("/synonyms")
# def create_synonymsArray(word, language):
#     return expander.get_similar_matrix(word, language)
