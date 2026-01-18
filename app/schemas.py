# app/schemas.py
from pydantic import BaseModel, Field


class EmailTextRequest(BaseModel):
    texto: str = Field(
        ...,
        description="Texto completo do e-mail que será classificado",
        min_length=5,
        max_length=15000,
        examples=["Olá, estou com problema na minha senha. Podem me ajudar?"]
    )


class ClassificationResponse(BaseModel):
    categoria: str
    resposta_sugerida: str