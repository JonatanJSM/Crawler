from fastapi import APIRouter
import core.utils.searcher.tokenizer as tokenizer


router = APIRouter()


LANGUAGES_PATH = "json/languages.json"


@router.get("/tokens")
async def create_tokens(input):
    return tokenizer.tokenize_input(input, LANGUAGES_PATH)
