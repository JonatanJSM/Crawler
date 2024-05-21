from pydantic import BaseModel


class Page(BaseModel):
    id: int
    url: str
    estado: bool
