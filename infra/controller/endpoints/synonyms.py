from fastapi import APIRouter
import utils.searcher.expander as expander


router = APIRouter()


@router.get("/synonyms")
async def create_synonymsArray(word, language):
    return expander.get_similar_matrix(word, language)
