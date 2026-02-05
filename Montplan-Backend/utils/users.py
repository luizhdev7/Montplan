# utils/users.py
import json
import os
from passlib.context import CryptContext

CAMINHO = os.path.join("database", "users.json")
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def buscar_usuario_por_email(email: str):
    """Retorna o usuário se existir, senão None"""
    if not os.path.exists(CAMINHO):
        return None

    with open(CAMINHO, "r") as f:
        dados = json.load(f)
        for u in dados["usuarios"]:
            if u["email"] == email:
                return u
    return None


def criar_usuario(nome: str, email: str, password: str):
    """Cria um novo usuário apenas se o email não existir"""
    if buscar_usuario_por_email(email):
        return None  # Indica que o usuário já existe

    if not os.path.exists(CAMINHO):
        with open(CAMINHO, "w") as f:
            json.dump({"ultimo_id": 0, "usuarios": []}, f)

    with open(CAMINHO, "r+") as f:
        dados = json.load(f)

        novo_id = dados["ultimo_id"] + 1
        senha_hash = pwd_context.hash(password)

        usuario = {
            "id": novo_id,
            "nome": nome,
            "email": email,
            "password": senha_hash
        }

        dados["usuarios"].append(usuario)
        dados["ultimo_id"] = novo_id

        f.seek(0)
        json.dump(dados, f, indent=4)
        f.truncate()

    return usuario
