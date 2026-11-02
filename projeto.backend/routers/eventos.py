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

@router.put("/{evento_id}")
def atualizar_evento(evento_id: int, evento: Evento):
    for i, evento_atual in enumerate(eventos):
        if evento_atual.id == evento_id:
            eventos[i] = evento
            return evento

    raise HTTPException(status_code=404, detail="Evento não encontrado")

@router.delete("/{evento_id}")
def excluir_evento(evento_id: int):
    for i, evento in enumerate(eventos):
        if evento.id == evento_id:
            eventos.pop(i)
            return {"mensagem": "Evento excluído com sucesso"}

    raise HTTPException(status_code=404, detail="Evento não encontrado")
