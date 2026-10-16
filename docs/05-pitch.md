# 05 — Pitch (3 minutos)

Roteiro de elevador para apresentar o PyTutor. Grave a tela do app durante a demo.

## Roteiro com tempos

### 0:00 – 0:30 | Problema

- "Quem começa a aprender Python trava em dúvidas básicas todos os dias."
- "IA genérica responde, mas às vezes inventa funções que não existem — e o iniciante não tem como perceber."
- "Falta uma resposta direta e confiável para quem está começando."

### 0:30 – 1:00 | Solução

- "PyTutor: um assistente que responde dúvidas de Python **apenas com base numa base de conhecimento curada**."
- "Quando não sabe, ele admite e aponta a documentação oficial. Zero invenção."
- "Cada resposta vem com exemplo curto de código e o próximo passo de estudo."

### 1:00 – 2:00 | Demo ao vivo

- Pergunta dentro do escopo: "Como pego o último item de uma lista?" → resposta com `lista[-1]`.
- Pergunta fora da base: "Como uso pandas para ler Excel?" → "Não tenho essa informação na minha base."
- Mostre a sidebar com os tópicos cobertos.

### 2:00 – 2:30 | Por que funciona

- Anti-alucinação em 3 camadas: regra no prompt, temperatura baixa, base pequena e validada por script.
- Context stuffing: simples, auditável, sem infraestrutura pesada.
- Base validada com `verificar_base.py` a cada mudança.
- Resultado do teste real: 9/10 respostas corretas, 3/3 recusas corretas, 0 alucinações e resistência a injeção de prompt.

### 2:30 – 3:00 | Próximos passos

- Expandir a base (orientação a objetos, bibliotecas populares).
- Migrar para busca vetorial (RAG) quando a base crescer.
- Coletar perguntas reais de usuários para priorizar novos tópicos.

## Checklist antes de gravar

- [ ] App rodando com a base e a API configuradas
- [ ] Conversa limpa antes de cada pergunta da demo
- [ ] Cronômetro: ensaie para caber em 3 minutos
- [x] Métricas reais no roteiro — teste de 16/10/2026 (docs/04-metricas.md)

**Fechamento (na sua voz, ~15 segundos):** "Escolhi Python porque é a linguagem que estou aprendendo agora, e percebi que quem está começando trava sempre nas mesmas dúvidas. O PyTutor é o assistente que eu queria ter tido quando comecei: responde direto, com exemplo de código, e não inventa nada — quando não sabe, ele fala."
