from fastapi import APIRouter, HTTPException
from models.model import Inscricao

router = APIRouter(
    prefix="/inscricoes",
    tags=["Inscrições"]
)

inscricoes = []

@router.get("/")
def listar_inscricoes():
    return inscricoes

@router.post("/", status_code=201)
def criar_inscricao(inscricao: Inscricao):
    inscricoes.append(inscricao)
    return inscricao

@router.put("/{inscricao_id}")
def atualizar_inscricao(inscricao_id: int, inscricao: Inscricao):
    for i, inscricao_atual in enumerate(inscricoes):
        if inscricao_atual.id == inscricao_id:
            inscricoes[i] = inscricao
            return inscricao

    raise HTTPException(status_code=404, detail="Inscrição não encontrada")

@router.delete("/{inscricao_id}")
def excluir_inscricao(inscricao_id: int):
    for i, inscricao in enumerate(inscricoes):
        if inscricao.id == inscricao_id:
            inscricoes.pop(i)
            return {"mensagem": "Inscrição excluída com sucesso"}

    raise HTTPException(status_code=404, detail="Inscrição não encontrada")
