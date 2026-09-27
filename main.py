from fastapi import FastAPI

app = FastAPI()

#FastAPI, registre a função home() como a função responsável por responder requisições GET enviadas para /.
@app.get("/")
def home():
    return {"message":"Iniciando minha primeira API"}

@app.get("/status")
def status():
    return{"status":"API funcionando"}

@app.get("/usuarios")
def usuarios():
    return{"usuarios":[]}

@app.get("/usuarios/{usuario_id}")
def buscar_usuarios(usuario_id:int):
    return {"usuario_id": usuario_id}

@app.get("/produtos")
def produtos():
    return{"produtos":[]}

@app.get("/produtos/{produto_id}")
def buscar_produtos(produto_id: int):
    return{
        "produto_id": produto_id,
        "nome": "Notebook"
    }

@app.get("categorias/{nome}")
def buscar_categoria(nome:str):
    return{
        "categoria":nome
    }

# metodos HTTP

# Request Body
# precisamos ensinar ao FASTAPI que um produto possui um nome e um preco
from pydantic import BaseModel

class Produto(BaseModel):
    nome:str
    preco:float

class Usuario(BaseModel):
    nome: str
    idade: int
    email: str 

# POST - criar alguma coisa
@app.post("usuarios")
def criar_usuario(usuario: Usuario):
    return{
        "message": "Usuario criado!",
        "usuario": usuario
    }

@app.post("/produtos")
def criar_produtos(produto:Produto):
    return {
        "message": "Produto criado!",
        "produto": produto
    }

# query parameters
@app.get("/produtos")
def listar_produtos(
    categoria:str | None = None,
    limit: int = 10,
    disponivel: bool = True
    ):
    return {
        "cateogoria": categoria,
        "limit": limit,
        "disponivel": disponivel
    }

@app.get("/usuarios")
def listar_usuarios(limit:int = 10):
    return{
        "quantidade": limit
    }

# Path + Query
@app.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    produto: Produto,
    notificar: bool = False
):
    return {
        "produto_id": produto_id,
        "produto": produto,
        "notificar": notificar
    }

# DELETE
@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id:int):
    return {
        "message": "Produto Removido",
        "produto_id": produto_id
    }

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id:int):
    return {
        "message": "Usuario Removido",
        "usuario_id": usuario_id
    }

# Tratando Erros 
from fastapi import HTTPException

app.get("/produtos/{produto_id}")
def buscar_produto(produto_id:int):

    if produto_id !=1:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return {
        "id": 1,
        "nome": "Notebook"
    }

app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id:int):

    if usuario_id <=0:
        raise HTTPException(
            status_code=404,
            detail="Usuario não encontrado"
        )

    return {
        "usuario_id":usuario_id
    }

# status codes 
from fastapi import status

@app.post(
    "/produtos",
    status_code=status.HTTP_201_CREATED
)
def criar_produto(produto: Produto):
    return produto

@app.delete(
    "/produtos/{produto_id}",
    status_code=status.HTTP_200_OK
)
def deletar_produto(produto_id: int):
    return {"deleted": produto_id}

# def ou async def
# não precisamos colocar async em tudo
@app.get("/")
async def home():
    return {"message":"Olá"}

