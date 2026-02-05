from pydantic import BaseModel
from datetime import date

class GastoCreate(BaseModel):
    nome: str
    valor: float
    data: date
    categoria: str | None = None


class GastoResponse(GastoCreate):
    id: int

    class Config:
        from_attributes = True
