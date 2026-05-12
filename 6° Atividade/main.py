from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from database import Base, engine, get_db
from schemas import ProdutoCreate, ProdutoResponse, ProdutoUpdate

Base.metadata.create_all(bind=engine)  # cria as tabelas ao iniciar

app = FastAPI(title="API de Catalogo de Produtos (SQLite)")


@app.get("/produtos12345", response_model=list[ProdutoResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)


@app.get("/produtos/{produto_id}", response_model=ProdutoResponse)
def buscar(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.buscar_produto(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.post("/produtos", response_model=ProdutoResponse, status_code=201)
def criar(dados: ProdutoCreate, db: Session = Depends(get_db)):
    return crud.criar_produto(db, dados)


@app.put("/produtos/{produto_id}", response_model=ProdutoResponse)
def substituir(produto_id: int, dados: ProdutoCreate,
               db: Session = Depends(get_db)):
    produto = crud.substituir_produto(db, produto_id, dados)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.patch("/produtos/{produto_id}", response_model=ProdutoResponse)
def atualizar(produto_id: int, dados: ProdutoUpdate,
              db: Session = Depends(get_db)):
    produto = crud.atualizar_produto(db, produto_id, dados)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


@app.delete("/produtos/{produto_id}", status_code=204)
def deletar(produto_id: int, db: Session = Depends(get_db)):
    print(produto_id)
    crud.deletar_produto(db, produto_id)