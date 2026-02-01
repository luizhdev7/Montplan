from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.users import pwd_context, CAMINHO
import json

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str


def buscar_usuario(email: str):
    with open(CAMINHO, "r") as f:
        dados = json.load(f)
    return next((u for u in dados["usuarios"] if u["email"] == email), None)

@router.post("/login")
def login(login_req: LoginRequest):
    usuario = buscar_usuario(login_req.email)
    if not usuario:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    if not pwd_context.verify(login_req.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")
    
    return {"msg": f"Bem-vindo {usuario['nome']}!"}
