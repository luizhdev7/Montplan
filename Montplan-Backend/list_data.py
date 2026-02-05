from db import SessionLocal
from models.gasto import Gasto
from models.salario import Salario

# Cria uma sessão com o banco
session = SessionLocal()

try:
    # Lista todos os gastos
    print("=== GASTOS ===")
    gastos = session.query(Gasto).all()
    for g in gastos:
        print(f"ID: {g.id}, Nome: {g.nome}, Valor: {g.valor}, Data: {g.data}, Categoria: {g.categoria}")

    # Lista todos os salários
    print("\n=== SALÁRIOS ===")
    salarios = session.query(Salario).all()
    for s in salarios:
        print(f"ID: {s.id}, Valor: {s.valor}, Data: {s.data}")

except Exception as e:
    print("Erro ao consultar dados:", e)

finally:
    session.close()
