from pydantic import BaseModel, AnyHttpUrl


class Page(BaseModel):
    id: int
    url: AnyHttpUrl
    estado: bool
