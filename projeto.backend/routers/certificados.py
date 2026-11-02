from fastapi import APIRouter, HTTPException
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

@router.put("/{certificado_id}")
def atualizar_certificado(certificado_id: int, certificado: Certificado):
    for i, certificado_atual in enumerate(certificados):
        if certificado_atual.id == certificado_id:
            certificados[i] = certificado
            return certificado

    raise HTTPException(status_code=404, detail="Certificado não encontrado")

@router.delete("/{certificado_id}")
def excluir_certificado(certificado_id: int):
    for i, certificado in enumerate(certificados):
        if certificado.id == certificado_id:
            certificados.pop(i)
            return {"mensagem": "Certificado excluído com sucesso"}

    raise HTTPException(status_code=404, detail="Certificado não encontrado")
