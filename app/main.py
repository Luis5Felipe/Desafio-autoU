from fastapi import UploadFile, File, Form, HTTPException, FastAPI
from fastapi import Request
from app.schemas import ClassificationResponse
from app.services.file_reader import read_txt, read_pdf
from app.services.nlp import preprocess
from app.services.classifier import classify_email
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Classificador de Emails")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/v1/classificar", response_model=ClassificationResponse)
async def classificar_email(
        file: UploadFile | None = File(None),
        text: str | None = Form(None)
):

    if not file and not text:
        raise HTTPException(
            status_code=400,
            detail="Envie um arquivo (.txt ou .pdf) ou texto direto."
        )

    if file:
        if file.filename.endswith(".txt"):
            content = await file.read()
            text = read_txt(content)

        elif file.filename.endswith(".pdf"):
            text = read_pdf(file.file)

        else:
            raise HTTPException(
                status_code=400,
                detail="Formato de arquivo não suportado."
            )

    clean_text = preprocess(text)
    categoria, resposta_sugerida = classify_email(clean_text)

    return {
        "categoria": categoria,
        "resposta_sugerida": resposta_sugerida
    }
