from schemas.salario_schema import SalarioCreate, SalarioResponse
from fastapi import APIRouter, HTTPException
from db import SessionLocal
from models.salario import Salario

router = APIRouter(prefix="/salarios", tags=["Salários"])


@router.get("/", response_model=list[SalarioResponse])
def listar_salarios():
    session = SessionLocal()
    salarios = session.query(Salario).all()
    session.close()
    return salarios



@router.post("/", response_model=SalarioResponse)
def criar_salario(salario: SalarioCreate):
    session = SessionLocal()
    novo_salario = Salario(**salario.model_dump())
    session.add(novo_salario)
    session.commit()
    session.refresh(novo_salario)
    session.close()
    return novo_salario

