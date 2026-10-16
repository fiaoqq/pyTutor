# 02 — Base de Conhecimento

## O que é

A base é o único material que o PyTutor pode usar para responder. Arquivo atual:

| Arquivo | Conteúdo |
|---------|----------|
| `data/base_conhecimento.json` | 11 tópicos sobre fundamentos de Python |

Cada tópico segue este schema:

```json
{
  "id": "listas",
  "titulo": "Listas",
  "nivel": "iniciante",
  "palavras_chave": ["lista", "append", "índice"],
  "explicacao": "Texto com a explicação do conceito.",
  "exemplo": "código Python curto",
  "erros_comuns": ["erro típico de quem está começando"]
}
```

## De onde vieram os dados

- Documentação oficial: [docs.python.org/pt-br/3/tutorial](https://docs.python.org/pt-br/3/tutorial/)
- Dúvidas comuns de iniciantes em cursos e comunidades.

✏️ **Personalize:** ajuste os tópicos para as dúvidas que você vê no seu contexto. Todo exemplo de código deve ser testado por você antes de entrar na base.

## Estratégia: por que sem RAG

O protótipo usa **context stuffing**: a base inteira é injetada no prompt a cada conversa.

- ✅ Simples de entender, testar e auditar.
- ✅ Base pequena cabe no contexto com folga.
- ❌ Não escala para milhares de tópicos.

**Quando migrar para RAG/vetores:** quando a base crescer a ponto de não caber (ou encarecer) no prompt. Registre essa evolução no pitch como próximo passo.

## Como expandir

1. Adicione o tópico no mesmo schema do JSON.
2. Rode a validação:

```bash
python src/verificar_base.py
```

3. Teste os exemplos de código do tópico.
4. Faça uma pergunta sobre o novo tópico no app e verifique se a resposta cita os dados corretos.

## Limites conhecidos

- Só cobre fundamentos; perguntas sobre bibliotecas retornam "não tenho essa informação".
- Dados curados manualmente ficam desatualizados se o Python mudar (raro nos fundamentos).

✏️ **Personalize:** registre aqui a data da última revisão dos dados e quem revisou.
