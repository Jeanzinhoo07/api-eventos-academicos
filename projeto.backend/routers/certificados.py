from fastapi import APIRouter
from models.model import Certificado

router = APIRouter(
    prefix="/certificados",
    tags=["Certificados"]
)

certificados = []

@router.get("/")
def listar_certificados():
    return certificados

@router.post("/", status_code=201)
def criar_certificado(certificado: Certificado):
    certificados.append(certificado)
    return certificado