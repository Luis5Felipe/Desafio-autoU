from pydantic import BaseModel

class ClassificationResponse(BaseModel):
    categoria: str
    resposta_sugerida: str