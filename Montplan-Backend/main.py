from fastapi import FastAPI


from routes.usuarios import router as usuarios_router
from routes.gastos import router as gastos_router
from routes.salarios import router as salarios_router
from routes.login import router as login_router


app = FastAPI(title="Montplan API")


@app.get("/")
def home():
    return {"Status": "Montplan rodando"}


app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(gastos_router, prefix="/gastos", tags=["Gastos"])
app.include_router(salarios_router, prefix="/salarios", tags=["Salários"])
app.include_router(login_router, prefix="/login", tags=["Login"])