# RAGPDF — Retrieval-Augmented Generation for PDFs

## Descrição (Português)

RAGPDF é uma ferramenta simples para transformar PDFs em um índice vetorial (Chroma) e permitir consultas em linguagem natural usando modelos generativos. O repositório inclui scripts para criar a base de dados vetorial a partir de PDFs na pasta `base/` e um script para interagir com o índice via prompt.

## Description (English)

RAGPDF is a small project to turn PDFs into a vector index (Chroma) and answer natural-language questions using generative models. The repo contains scripts to build the vector DB from PDFs in `base/` and a script to interact with the index from a prompt.

## Sumário / Contents

- `main.py` — entrypoint to ask questions interactively.
- `criar_db.py` — builds the Chroma DB from PDFs stored in `base/`.
- `requirements.txt` — Python dependencies.
- `base/` — folder containing source PDFs.
- `db/` — folder where Chroma stores the SQLite/db shard files (ignored by git by default).
- `gabarito/` — auxiliary folder (currently empty).

## Requisitos / Requirements

- Python 3.10+ (recommended)
- Dependências listadas em `requirements.txt`

## Instalação / Setup

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` com as variáveis necessárias (veja `.env.example`).

## Configuração de ambiente / Environment

Copie o `.env.example` para `.env` e preencha as chaves necessárias. Exemplo de variáveis que podem ser necessárias (ajuste conforme seu provedor e código):

```
GOOGLE_API_KEY=your_google_api_key_here
```

## Construir a base de dados / Build the DB

Coloque seus PDFs em `base/` e execute:

```bash
python3 criar_db.py
```

Isso processará os PDFs e criará os arquivos do Chroma em `db/`. Por padrão `db/` não é versionado — recomendamos recriar o DB localmente usando `criar_db.py`.

## Executar / Run

Depois de criar/ter o DB, execute:

```bash
python3 main.py
```

Siga as instruções no prompt para fazer perguntas ao sistema.

## Estrutura do projeto / Project structure

- `main.py` — interativo
- `criar_db.py` — pipeline de ingestão e criação do Chroma DB
- `requirements.txt` — dependências
- `base/` — PDFs fonte
- `db/` — dados do Chroma (não versionados)

## Notas sobre dados / Data notes

- `db/` contém `chroma.sqlite3` e arquivos binários (`*.bin`) usados pelo Chroma. Esses arquivos podem ser grandes e são gerados automaticamente por `criar_db.py`.
- Se preferir versionar um subconjunto do DB, ajuste o `.gitignore` conforme necessário.

## Contribuição / Contributing

Pull requests e issues são bem-vindos. Adicione instruções adicionais aqui conforme necessário.
