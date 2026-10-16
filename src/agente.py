"""Lógica compartilhada do PyTutor: base de conhecimento + chamada à LLM.

Usada por src/app.py (chat) e src/avaliar.py (avaliação automática).
"""

import glob
import json
import os

from openai import OpenAI

PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELO_PADRAO = "gpt-4o-mini"


def carregar_env(caminho=None):
    """Carrega um arquivo .env (uma VARIAVEL=valor por linha) para os.environ.

    Variáveis já definidas no ambiente têm prioridade.
    """
    caminho = caminho or os.path.join(PASTA_RAIZ, ".env")
    if not os.path.exists(caminho):
        return
    with open(caminho, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha or linha.startswith("#") or "=" not in linha:
                continue
            chave, valor = linha.split("=", 1)
            os.environ.setdefault(chave.strip(), valor.strip().strip('"').strip("'"))


def carregar_base(pasta=None):
    """Carrega todos os JSONs da pasta data/ como base de conhecimento."""
    pasta = pasta or os.path.join(PASTA_RAIZ, "data")
    base = []
    for caminho in sorted(glob.glob(os.path.join(pasta, "*.json"))):
        with open(caminho, encoding="utf-8") as arquivo:
            base.append(json.load(arquivo))
    return base


def montar_system_prompt(base):
    """Junta o prompt do agente com a base de conhecimento (context stuffing)."""
    caminho = os.path.join(PASTA_RAIZ, "src", "system_prompt.txt")
    with open(caminho, encoding="utf-8") as arquivo:
        prompt = arquivo.read()
    dados = json.dumps(base, ensure_ascii=False)
    return f"{prompt}\n\n## BASE DE CONHECIMENTO\n{dados}"


def montar_cliente():
    """Cliente compatível com OpenAI. Funciona com OpenAI, Groq, Ollama e afins."""
    return OpenAI(
        base_url=os.getenv("OPENAI_BASE_URL") or "https://api.openai.com/v1",
        api_key=os.getenv("OPENAI_API_KEY") or "ollama",
    )


def responder(cliente, modelo, system_prompt, mensagens):
    historico = [{"role": "system", "content": system_prompt}] + mensagens
    resposta = cliente.chat.completions.create(
        model=modelo,
        messages=historico,
        temperature=0.2,  # baixa criatividade: menos risco de invenção
    )
    return resposta.choices[0].message.content
