from fastapi import APIRouter
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