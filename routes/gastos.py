from schemas.gasto_schema import GastoCreate, GastoResponse
from fastapi import APIRouter, HTTPException
from db import SessionLocal
from models.gasto import Gasto

router = APIRouter(prefix="/gastos", tags=["Gastos"])


@router.get("/", response_model=list[GastoResponse])
def listar_gastos():
    session = SessionLocal()
    gastos = session.query(Gasto).all()
    session.close()
    return gastos



@router.post("/", response_model=GastoResponse)
def criar_gasto(gasto: GastoCreate):
    session = SessionLocal()
    novo_gasto = Gasto(**gasto.model_dump())
    session.add(novo_gasto)
    session.commit()
    session.refresh(novo_gasto)
    session.close()
    return novo_gasto
 
