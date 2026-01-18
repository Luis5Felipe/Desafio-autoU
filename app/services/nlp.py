import spacy

nlp = spacy.load("pt_core_news_sm")

def preprocess(text: str) -> str:
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)
