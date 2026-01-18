from PyPDF2 import PdfReader

def read_txt(content: bytes) -> str:
    return content.decode("utf-8")

def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
