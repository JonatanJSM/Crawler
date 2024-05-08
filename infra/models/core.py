from pydantic import BaseModel


class Core(BaseModel):
    id: int
    corename: str
    estado: bool
