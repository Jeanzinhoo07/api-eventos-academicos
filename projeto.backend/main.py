from fastapi import FastAPI

from routers import usuarios
from routers import eventos
from routers import inscricoes
from routers import certificados

app = FastAPI(
    title="API Eventos Acadêmicos",
    version="1.0.0"
)

app.include_router(usuarios.router)
app.include_router(eventos.router)
app.include_router(inscricoes.router)
app.include_router(certificados.router)

@app.get("/")
def inicio():
    return {"mensagem": "API de Eventos Acadêmicos"}