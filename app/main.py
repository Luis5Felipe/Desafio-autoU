from fastapi import FastAPI, UploadFile, File
from app.services.file_reader import read_txt, read_pdf
from app.services.nlp import preprocess
from app.services.classifier import classify_email
app = FastAPI(title="Classificador de Emails")

@app.post("/classificar")
async def classificar_email(file: UploadFile = File(...)):
    if file.filename.endswith(".txt"):
        content = await file.read()
        text = read_txt(content)
    elif file.filename.endswith(".pdf"):
        text = read_pdf(file.file)
    else:
        return {"erro": "Formato não suportado"}
    clean_text = preprocess(text)
    categoria, resposta_sugerida = classify_email(clean_text)

    return {
        "categoria": categoria,
        "resposta_sugerida": resposta_sugerida
    }
