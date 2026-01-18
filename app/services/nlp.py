import spacy
import subprocess

_nlp = None

def get_nlp():
    try:
        return spacy.load("pt_core_news_sm")
    except OSError:
        subprocess.run(["python", "-m", "spacy", "download", "pt_core_news_sm"])
        return spacy.load("pt_core_news_sm")

def preprocess(text: str) -> str:
    nlp = get_nlp()
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)
