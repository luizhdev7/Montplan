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
 
 
 
@router.put("/{gasto_id}", response_model=GastoResponse)
def atualizar_gasto(gasto_id: int, gasto_atualizado: GastoCreate):
    session = SessionLocal()
    
    gasto = session.query(Gasto).filter(Gasto.id == gasto_id).first()
    if not gasto:
        session.close()
        raise HTTPException(status_code=404, detail="Gasto não encontrado")
    
    for key, value in gasto_atualizado.model_dump().items():
        setattr(gasto, key, value)
    
    session.commit()
    session.refresh(gasto)
    session.close()
    return gasto



@router.delete("/{gasto_id}", response_model=dict)
def deletar_gasto(gasto_id: int):
    session = SessionLocal()
    
    gasto = session.query(Gasto).filter(Gasto.id == gasto_id).first()
    if not gasto:
        session.close()
        raise HTTPException(status_code=404, detail="Gasto não encontrado")
    
    session.delete(gasto)
    session.commit()
    session.close()
    return {"detail": "Gasto deletado com sucesso"}
