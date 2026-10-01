from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nome: str
    email: str


class Evento(BaseModel):
    id: int
    titulo: str
    descricao: str
    capacidade: int


class Inscricao(BaseModel):
    id: int
    usuario_id: int
    evento_id: int


class Certificado(BaseModel):
    id: int
    usuario_id: int
    evento_id: int