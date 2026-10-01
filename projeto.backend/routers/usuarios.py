from fastapi import APIRouter, HTTPException
from models.model import Usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

usuarios = []


@router.get("/")
def listar_usuarios():
    return usuarios


@router.post("/", status_code=201)
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario


@router.get("/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )


@router.put("/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario_atualizado: Usuario):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[i] = usuario_atualizado
            return usuario_atualizado

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )


@router.delete("/{usuario_id}", status_code=204)
def excluir_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuarios.remove(usuario)
            return

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )