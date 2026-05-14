from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProdutoCreate(BaseModel):
    nome:    str
    preço: float
    categoria: str
    quantidade: int

class ProdutoUpdate(BaseModel):
    nome:       Optional[str]  = None
    preço:      Optional[float]  = None
    categoria:  Optional[str] = None
    quantidade: Optional[int] = None

class ProdutoResponse(BaseModel):
    id:         int
    nome:       str
    categoria:  str
    preço:      float
    quantidade: int

    model_config = ConfigDict(from_attributes=True)
