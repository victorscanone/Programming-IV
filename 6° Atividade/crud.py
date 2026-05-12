from sqlalchemy.orm import Session
from models import Produto
from schemas import ProdutoCreate, ProdutoUpdate


def listar_produtos(db: Session):
    return db.query(Produto).all()


def buscar_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()


def criar_produto(db: Session, dados: ProdutoCreate):
    produto = Produto(**dados.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


def atualizar_produto(db: Session, produto_id: int, dados: ProdutoUpdate):
    produto = buscar_produto(db, produto_id)
    if not produto:
        return None
    atualizacoes = dados.model_dump(exclude_unset=True)
    for campo, valor in atualizacoes.items():
        # tarefa.campo = valor
        setattr(produto, campo, valor)
    db.commit()
    db.refresh(produto)
    return produto


def substituir_produto(db: Session, produto_id: int, dados: ProdutoCreate):
    produto = buscar_produto(db, produto_id)
    if not produto:
        return None
    produto.titulo    = dados.titulo
    produto.descricao = dados.descricao
    produto.concluida = False
    db.commit()
    db.refresh(produto)
    return produto


def deletar_produto(db: Session, produto_id: int):
    produto = buscar_produto(db, produto_id)
    if produto:
        db.delete(produto)
        db.commit()
    else:
        print(f"Produto de id {produto_id} não encontrada para deletar.")
    return produto