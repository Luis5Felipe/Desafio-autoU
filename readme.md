# Classificador de Emails

Projeto simples de classificação de e-mails como PRODUTIVO ou IMPRODUTIVO, usando FastAPI, Transformers e NLP (Spacy).
Aceita texto direto ou arquivos .txt e .pdf para análise.

Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- PyPDF2
- Transformers-Huggingface-hub
- Spacy (pt_core_news_sm)

# Como Executar Localmente

### Clone o repositório
```
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto
```

### Crie e ative um ambiente virtual

```
python -m venv .venv
```

### windows 

````
.venv\Scripts\activate
````

### Linux

````
source .venv/bin/activate
````

### Instale as dependências

````
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
````

### Execute a aplicação

```
uvicorn app.main:app --reload
```

### Acesse a aplicação

```
http://127.0.0.1:8000/
```

# Estrutura do Projeto

````
.
├── app/
│   ├── main.py            # FastAPI app principal
│   ├── services/
│   │   ├── classifier.py  # Função classify_email
│   │   ├── file_reader.py # Funções read_txt e read_pdf
│   │   └── nlp.py         # Função preprocess
│   └── schemas.py         # Pydantic ClassificationResponse
├── static/                # CSS, JS e imagens
├── templates/             # Arquivos HTML (index.html)
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
````
# Exemplos de Uso

Texto enviado pelo formulário da página web:
````text
"Olá, estou com problemas para acessar minha conta e preciso de ajuda urgente."
````
### Resposta esperada

````json
{
  "categoria": "PRODUTIVO",
  "resposta_sugerida": "Olá, obrigado pelo contato. Recebemos sua solicitação e nossa equipe já está analisando para retornar o mais breve possível."
}
````

## Exemplo 2: Arquivo PDF ou TXT

- Faça upload de um arquivo .txt ou .pdf pelo formulário.
- O endpoint /api/v1/classificar retorna JSON com categoria e resposta sugerida

# Observações

- Apenas arquivos .txt e .pdf são suportados.
- O classificador utiliza Zero-Shot Classification, então os resultados podem variar conforme o texto.
- Para textos muito longos, o processamento pode demorar um pouco.

