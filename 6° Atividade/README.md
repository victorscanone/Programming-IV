# CRUD de Produtos utilizando o FastAPI

#Integrante: Victor Scanone

---

# Descrição
API para o gerenciamento de produtos, utilizando o SQLite e o FastAPI.

Permite buscar, listar, criar, atualizar e remover produtos.

---

# Como executar?

Escreva no terminal:
bash pip install fastapi uvicorn sqlalchemy uvicorn main:app --reload 

Depois vá para essa URL em um navegador:
http://127.0.0.1:8000/docs

---

#Rotas

| Método | Rota | Função |
|--------|------|--------|
| GET | /produtos | Listar produtos |
| GET | /produtos/{id} | Buscar por ID |
| POST | /produtos | Criar produto |
| PUT | /produtos/{id} | Atualizar tudo |
| PATCH | /produtos/{id} | Atualizar parcial |
| DELETE | /produtos/{id} | Deletar |

---

#Decisões

- SQLite como banco de dados
- Todos os campos obrigatórios na criação
- PATCH permite campos opcionais
- Retorna 404 caso o produto não existe

---

# Estrutura

- main.py
- models.py
- schemas.py
- crud.py
- database.py

---