from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    nome:str
    preco:float
    estoque:int

produtos = {
    1: Produto(
        nome="Notebook",
        preco=4500,
        estoque=10
    )
}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id:int):

    if produto_id !=1:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return produtos[produto_id]

@app.post(
    "/produtos",
    status_code=status.HTTP_201_CREATED
)
def criar_produto(produto: Produto):
    novo_id = len(produtos) + 1 
    produtos[novo_id] = produto

    return {
        "id": novo_id,
        "produto": produto
    }

@app.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    produto: Produto
):

    if produto_id not in produtos:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    produtos[produto_id] = produto

    return produto


@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):

    if produto_id not in produtos:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    del produtos[produto_id]

    return {
        "message": "Produto removido"
    }