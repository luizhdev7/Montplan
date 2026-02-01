from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.users import criar_usuario

router = APIRouter()

class UsuarioRequest(BaseModel):
    nome: str
    email: str
    password: str

@router.post("/usuarios")
def cadastro_usuario(usuario: UsuarioRequest):
    novo_usuario = criar_usuario(usuario.nome, usuario.email, usuario.password)
    if novo_usuario["id"] != 1:  # se o email já existia
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return {"msg": f"Usuário {novo_usuario['nome']} criado com sucesso!", "id": novo_usuario["id"]}
