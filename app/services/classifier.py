from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = ["Produtivo", "Improdutivo"]

def classify_email(text: str) -> str:
    result = classifier(text, LABELS)
    return result["labels"][0]
