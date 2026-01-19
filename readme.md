# Classificador de E-mails Inteligente

Este projeto é uma ferramenta de triagem automática de e-mails desenvolvida com **FastAPI**. Ele classifica mensagens como **PRODUTIVO** (mensagens que requerem ação ou suporte técnico) ou **IMPRODUTIVO** (saudações, agradecimentos e mensagens de cortesia).

A solução utiliza uma abordagem híbrida: **Heurística de Palavras-Chave** para detecção imediata e **Inteligência Artificial (NLP)** para análise de contexto profundo.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e de alta performance.
- **spaCy (pt_core_news_sm)**: Processamento de Linguagem Natural e lematização em português.
- **Hugging Face Inference API**: Modelo `mDeBERTa-v3-base-mnli-xnli` para classificação Zero-Shot.
- **PyPDF2**: Biblioteca para extração de texto de arquivos PDF.
- **Python-dotenv**: Gerenciamento seguro de variáveis de ambiente e tokens.
- **Deploy**: Render

---

## Exemplos de Resposta

````json
{
  "categoria": "PRODUTIVO",
  "resposta_sugerida": "Recebemos sua dúvida/suporte e nossa equipe já está analisando."
}
````

````json
{
  "categoria": "IMPRODUTIVO",
  "resposta_sugerida": "Obrigado pela sua mensagem!"
}
````

# Estrutura do Projeto

````tree
.
├── app/
│   ├── main.py            # Endpoints da API e rotas do sistema
│   ├── schemas.py         # Modelos de dados (Pydantic)
│   └── services/
│       ├── classifier.py  # Lógica híbrida (Keywords + IA via Requests)
│       ├── nlp.py         # Pré-processamento e lematização com spaCy
│       └── file_reader.py # Extração de texto de PDFs e TXTs
├── static/                # Interface (CSS, JS)
├── templates/             # index.html (Front-end)
├── .env                   # Variáveis sensíveis (não enviado ao Git)
└── requirements.txt       # Dependências do projeto
````

## Como Executar Localmente

### 1. Requisitos
* Python 3.10 ou superior.
* Token de acesso (Read) do [Hugging Face](https://huggingface.co/settings/tokens).

### 2. Instalação

```bash
# Clone o repositório
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto

# Crie e ative o ambiente virtual
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
````

### 3. Configuração (.env)

Crie um arquivo chamado .env na raiz do projeto e adicione seu token:
Snippet de código

```bash
HF_TOKEN=seu_token_aqui
```

### 4. Execução

```Bash
uvicorn app.main:app --reload
Acesse em: http://127.0.0.1:8000
```