from fastapi import FastAPI
from models.page import Page
from crawler.engine import Engine

app = FastAPI()


@app.post("/pages")
def create_page(page: Page):
    urls = ["https://www.wagslane.dev/"]
    engine = Engine(urls)
    engine.start()
    return {"page": page}
