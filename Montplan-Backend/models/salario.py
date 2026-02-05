from db import Base
from sqlalchemy import Column, Integer, Float, Date

class Salario(Base):
    __tablename__ = "salarios"

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)
