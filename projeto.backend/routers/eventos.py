from fastapi import APIRouter, HTTPException
from models.model import Evento

router = APIRouter(
    prefix="/eventos",
    tags=["Eventos"]
)

eventos = []

@router.get("/")
def listar_eventos():
    return eventos

@router.post("/", status_code=201)
def criar_evento(evento: Evento):
    eventos.append(evento)
    return evento