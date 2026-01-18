from transformers import pipeline
import torch
import logging

classifier = pipeline(
    "zero-shot-classification",
    model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli",
    device=0 if torch.cuda.is_available() else -1
)

def classify_email(email_content: str):
    if not classifier:
        return "Erro", "Modelo de IA não disponível.", ""

    critical_keywords = [
        "solicitação", "pedido", "suporte", "ajuda", "dúvida", "problema", "erro",
        "preciso", "necessito", "gostaria", "poderia", "status", "extrato", "fatura",
        "boleto", "senha", "acesso", "login", "conta", "cancelar", "reembolso", "troca",
        "devolução", "não consigo", "urgente", "parado", "bloqueado", "estornar"
    ]

    email_lower = email_content.lower()

    for keyword in critical_keywords:
        if keyword in email_lower:
            return (
                "PRODUTIVO",
                "Olá, obrigado pelo seu e-mail. Estamos analisando sua solicitação e retornaremos em breve com uma atualização."
            )
    candidate_labels = [
        "saudação, cortesia, agradecimento, elogio ou encerramento sem ação",
        "solicitação de ajuda, problema técnico, dúvida, pedido ou necessidade de intervenção"
    ]

    hypothesis_template = "Este e-mail é sobre {}."

    try:
        result = classifier(
            email_content,
            candidate_labels=candidate_labels,
            multi_label=True,
            hypothesis_template=hypothesis_template
        )

        # probabilities_str = "\n".join(
        #     f"- {label.split(',')[0].strip().capitalize()}: {score:.2%}"
        #     for label, score in zip(result['labels'], result['scores'])
        # )

        try:
            action_index = result['labels'].index(candidate_labels[1])
            action_score = result['scores'][action_index]
        except ValueError:
            action_score = 0.0

        print(action_score)

        if action_score > 0.6:
            categoria = "PRODUTIVO"
            resposta = (
                "Olá, obrigado pelo contato. Recebemos sua solicitação e "
                "nossa equipe já está analisando para retornar o mais breve possível."
            )
        else:
            categoria = "IMPRODUTIVO"
            resposta = (
                "Olá! Muito obrigado pela mensagem positiva. "
                "Ficamos felizes em ajudar. Tenha um ótimo dia! 😊"
            )
        return categoria, resposta

    except Exception as e:
        logging.error(f"Erro na classificação zero-shot: {e}")
        return "Erro", "Ocorreu um erro ao processar o e-mail.", ""