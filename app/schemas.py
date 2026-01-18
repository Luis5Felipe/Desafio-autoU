from pydantic import BaseModel, Field

class ClassificationResponse(BaseModel):
    categoria: str
    resposta_sugerida: str