# 🐍 PyTutor — Assistente Virtual com IA para aprender Python

Projeto do Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"** (DIO).

## Problema

Quem começa a aprender Python trava em dúvidas básicas: erro de sintaxe, diferença entre `=` e `==`, como usar listas. IAs genéricas respondem bem, mas às vezes **inventam funções e comportamentos** que não existem — e quem está começando não tem como perceber.

## Solução

**PyTutor**: assistente que responde dúvidas de Python **somente com base numa base de conhecimento curada**. Quando não sabe, ele admite e sugere onde procurar. Sem respostas inventadas.

- Escopo: fundamentos de Python (11 tópicos na base).
- Comportamento: resposta direta + exemplo de código + próximo passo de estudo.
- Segurança: regra anti-alucinação no prompt + temperatura baixa + base pequena e verificável.

## Como rodar

```bash
# 1. Ambiente
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Verificar a base de conhecimento (sem LLM)
python src/verificar_base.py

# 3a. Usar com OpenAI
export OPENAI_API_KEY="sua-chave-aqui"
streamlit run src/app.py

# 3b. OU usar com Ollama local (grátis, sem chave)
ollama pull llama3.1
export OPENAI_BASE_URL="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"
export OPENAI_MODEL="llama3.1"
streamlit run src/app.py
```

Variáveis de ambiente suportadas: `OPENAI_API_KEY`, `OPENAI_BASE_URL` (opcional, qualquer API compatível com OpenAI), `OPENAI_MODEL` (padrão: `gpt-4o-mini`). Em vez de exportar, você pode defini-las num arquivo `.env` na raiz do projeto (já está no `.gitignore`).

Para rodar a avaliação completa (14 perguntas): `python src/avaliar.py` — gera o transcript em `docs/resultados_teste.md`.

## Estrutura

```
assistente-virtual-ia/
├── README.md
├── requirements.txt
├── data/
│   └── base_conhecimento.json      # 11 tópicos curados sobre Python
├── docs/
│   ├── 01-documentacao-agente.md   # Caso de uso, persona, arquitetura
│   ├── 02-base-conhecimento.md     # Estratégia de dados
│   ├── 03-prompts.md               # Engenharia de prompts + edge cases
│   ├── 04-metricas.md              # 14 perguntas de teste + métricas
│   └── 05-pitch.md                 # Roteiro do pitch de 3 min
└── src/
    ├── app.py                      # Aplicação Streamlit
    ├── agente.py                   # Lógica compartilhada (base + chamada à LLM)
    ├── avaliar.py                  # Roda as 14 perguntas de avaliação
    ├── system_prompt.txt           # Prompt do agente (fonte viva)
    └── verificar_base.py           # Valida a base de conhecimento
```

## Exemplos de perguntas para testar

Dentro do escopo:
- "Como crio uma lista e adiciono um item?"
- "Meu programa deu IndexError, o que significa?"
- "Para que serve o return?"
- "Como instalar uma biblioteca sem bagunçar meu Python?"

Fora do escopo (o agente deve admitir):
- "Como uso pandas para ler Excel?" — não está na base
- "Quem ganhou a Copa de 2022?" — fora do tema

## Os 6 passos do desafio

| # | Passo | Onde está |
|---|-------|-----------|
| 1 | Documentação | [docs/01-documentacao-agente.md](docs/01-documentacao-agente.md) |
| 2 | Base de conhecimento | [data/base_conhecimento.json](data/base_conhecimento.json) + [docs/02](docs/02-base-conhecimento.md) |
| 3 | Prompts | [src/system_prompt.txt](src/system_prompt.txt) + [docs/03](docs/03-prompts.md) |
| 4 | Aplicação funcional | [src/app.py](src/app.py) |
| 5 | Avaliação e métricas | [docs/04-metricas.md](docs/04-metricas.md) |
| 6 | Pitch | [docs/05-pitch.md](docs/05-pitch.md) |

## Créditos

- Desafio: [digitalinnovationone/dio-lab-bia-do-futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro)
- Referência de implementação: [falvojr/dio-lab-bia-do-futuro](https://github.com/falvojr/dio-lab-bia-do-futuro)
