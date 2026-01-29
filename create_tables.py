from db import Base, engine
from models.gasto import Gasto
from models.salario import Salario

Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")
