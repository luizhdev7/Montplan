from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from utils.users import criar_usuario, buscar_usuario_por_email, listar_usuarios

router = APIRouter()

class UsuarioRequest(BaseModel):
    nome: str
    email: EmailStr
    password: str


@router.post("/usuarios")
def cadastro_usuario(usuario: UsuarioRequest):
    if buscar_usuario_por_email(usuario.email):
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_usuario = criar_usuario(
        usuario.nome,
        usuario.email,
        usuario.password
    )

    return {
        "msg": f"Usuário {novo_usuario['nome']} criado com sucesso!",
        "id": novo_usuario["id"]
    }


@router.get("/")
def listar():
    return listar_usuarios()
