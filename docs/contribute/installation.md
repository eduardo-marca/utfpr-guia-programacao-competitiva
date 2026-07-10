# Instalação

Este guia tem como objetivo mostar como instalar, configurar e rodar o repositório locamente.

## Pré-requisitos
- Git
- Python 3.11+
- IDE (por exemplo, VS Code)

## Clonando o Repositório
```bash
`git clone https://github.com/eduardo-marca/utfpr-guia-programacao-competitiva` 
`cd utfpr-guia-programacao-competitiva`
```

## Criando Ambiente Vitual

Esse repositório utiliza um ambiente virtual python.

### Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows (Não Testado)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Instalando dependências
```bash
pip install -r requirements.txt
```

## Executar localmente

```bash
mkdocs serve
```

Abra:

http://127.0.0.1:8000

## Testando
Tente editar o arquivo `docs/index.md` e salvar para testar se o site local atualiza automaticamente.
