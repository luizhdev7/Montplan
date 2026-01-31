from pydantic import BaseModel
from datetime import date

class SalarioCreate(BaseModel):
    valor: float
    data: date

class SalarioResponse(SalarioCreate):
    id: int

    class Config:
        from_attributes = True
