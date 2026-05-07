from fastapi import APIRouter
from pydantic import BaseModel, Field

registro_foco = APIRouter(prefix="/registro", tags=["registro_foco"])

class RegistroFoco(BaseModel):
    nivel_foco: int = Field(ge=1, le=5, description="Deve estar entre 1 e 5")
    tempo_minutos: int
    title: str
    comentario: str


@registro_foco.post("/")
async def inserirDados(registro_foco: RegistroFoco):
    if (RegistroFoco.nivel_foco <= 0 and registro_foco.nivel_foco > 5):

    return ["Dados cadastrados com sucesso!"]