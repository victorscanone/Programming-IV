from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id         = Column(Integer, primary_key=True, index=True)
    nome       = Column(String,  nullable=False)
    preço      = Column(float,  default=0.0)
    categoria  = Column(String, default="")
    quantidade = Column(Integer, default=0)