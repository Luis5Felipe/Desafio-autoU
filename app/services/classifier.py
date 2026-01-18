import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("HF_TOKEN")
if not API_TOKEN:
    raise ValueError("HF_TOKEN não encontrado. Coloque no .env ou variáveis de ambiente.")

API_URL = "https://router.huggingface.co/hf-inference/models/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


def classify_email(email_content: str):

    email_lower = email_content.lower()

    critical_keywords = [
        "erro", "bug", "falha", "não consigo", "problema técnico",
        "fatura", "senha", "estorno", "cancelar"
    ]

    for keyword in critical_keywords:
        if keyword in email_lower:
            return "PRODUTIVO", "Olá! Recebemos sua solicitação técnica."

    candidate_labels = ["agradecimento ou elogio", "duvida ou suporte", "saudacao"]
    payload = {
        "inputs": email_content,
        "parameters": {
            "candidate_labels": candidate_labels,
            "multi_label": True
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        result = response.json()

        if response.status_code != 200:
            logging.error(f"Erro da API: {result}")
            return "Erro", "IA indisponível no momento."

        if isinstance(result, list):
            result = result[0]

        if 'label' in result:
            top_label = result['label']
            top_score = result['score']

        elif 'labels' in result:
            top_label = result['labels'][0]
            top_score = result['scores'][0]
        else:
            logging.error(f"Formato desconhecido: {result}")
            return "Erro", "Resposta da IA em formato inesperado."

        print(f"IA identificou: {top_label} (Confiança: {top_score:.2f})")

        if "duvida" in top_label or "solicitacao" in top_label:
            return "PRODUTIVO", "Recebemos sua solicitação e nossa equipe já está analisando."
        else:
            return "IMPRODUTIVO", "Obrigado pela sua mensagem! Tenha um ótimo dia."

    except Exception as e:
        logging.error(f"Falha crítica: {e}")
        return "Erro", "Falha ao processar e-mail."