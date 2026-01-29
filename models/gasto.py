from db import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
    categoria = Column(String, nullable=True)
