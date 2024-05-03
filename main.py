from fastapi import FastAPI
from models.page import Page
from crawler.engine import Engine
import searcher.tokenizer as tokenizer
import searcher.expander as expander


app = FastAPI()


LANGUAGES_PATH = "json/languages.json"


@app.post("/pages")
def create_page(page: Page):
    urls = ["https://www.wagslane.dev/"]
    engine = Engine(urls)
    engine.start()
    return {"page": page}


@app.get("/tokens")
def create_tokens(input):
    return tokenizer.tokenize_input(input, LANGUAGES_PATH)


@app.get("/synonyms")
def create_synonymsArray(word, language):
    return expander.get_similar_matrix(word, language)
