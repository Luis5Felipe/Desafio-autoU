from fastapi import FastAPI, UploadFile, File
from app.services.file_reader import read_txt, read_pdf
from app.services.nlp import preprocess
from app.services.classifier import classify_email
from app.services.responder import generate_response

app = FastAPI(title="Classificador de Emails")

@app.post("/classificar")
async def classificar_email(file: UploadFile = File(...)):
    if file.filename.endswith(".txt"):
        text = read_txt(await file.read())
    elif file.filename.endswith(".pdf"):
        text = read_pdf(file.file)
    else:
        return {"erro": "Formato não suportado"}

    clean_text = preprocess(text)
    category = classify_email(clean_text)
    response = generate_response(category)

    return {
        "categoria": category,
        "resposta_sugerida": response
    }
