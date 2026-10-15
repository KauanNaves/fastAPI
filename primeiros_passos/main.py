# Primeiros Passos
from fastapi import FastAPI

app = FastAPI()

# URL completa -> https://127.0.0.1:8000/
# Path -> se refere à última parte da URL a partir da primeira / -> "/"
""" Operação -> se refere aos métodos HTTP
    POST - Criar dados
    GET - Ler dados
    PUT - Atualizar dados
    DELETE - Apagar dados

    E os menos comuns
    OPTIONS
    HEAD
    PATCH
    TRACE

"""

@app.get("/")
async def home():
    return {"home": "Página Home",
            "message": "Hello, world!"}

