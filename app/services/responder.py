def generate_response(category: str) -> str:
    if category == "Produtivo":
        return (
            "Olá! Obrigado pelo seu contato. "
            "Recebemos sua mensagem e retornaremos em breve com a solução."
        )
    else:
        return (
            "Olá! Agradecemos sua mensagem. "
            "Ficamos felizes pelo seu contato!"
        )
