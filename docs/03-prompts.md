# 03 — Prompts do Agente

O prompt completo e editável vive em **[`src/system_prompt.txt`](../src/system_prompt.txt)** — é ele que o app carrega em tempo de execução. Este documento explica as decisões por trás dele e mostra os cenários de uso.

> Não duplique o prompt aqui: edite o `.txt` e o app já usa a versão nova.

## Estrutura do system prompt

| Bloco | Para que serve |
|-------|----------------|
| Objetivo | Diz em uma frase o que o agente faz. |
| Regras de comportamento | Restrições: só a base, admitir quando não sabe, nunca inventar, tom e formato, anti-injeção (regra 9). |
| Formato da resposta | Padroniza a saída: resposta + exemplo + próximo passo. |
| Exemplos de interação | Few-shot: um caso dentro do escopo e um fora. |
| Edge cases | Instruções para situações limite. |

### Decisões principais

- **Regra 1 (só a base):** é o coração anti-alucinação. Sem ela, a LLM responde do conhecimento geral e o iniciante não sabe o que é confiável.
- **Regra 2 (fórmula de recusa):** a frase "Não tenho essa informação na minha base de conhecimento." é fixa de propósito — facilita medir recusas corretas na avaliação.
- **Regra 5 (exemplo curto):** máximo 10 linhas; exemplos longos intimidam iniciantes.
- **Temperatura 0.2 no app:** reforça o determinismo fora do prompt.

## Exemplos de interação

**1. Dúvida dentro do escopo**

- Entrada: "Como pego o último item de uma lista?"
- Saída esperada: explica índice negativo (`lista[-1]`), com exemplo, e sugere o tópico de listas.

**2. Tópico ausente da base**

- Entrada: "Como uso pandas para ler um Excel?"
- Saída esperada: admite que não tem a informação na base e sugere a documentação oficial. **Não** ensina pandas.

**3. Fora do tema**

- Entrada: "Quem ganhou a Copa de 2022?"
- Saída esperada: recusa educada, informa que o escopo é Python e oferece tópicos da base.

## Edge cases tratados

| Situação | Comportamento definido |
|----------|------------------------|
| Tópico ausente da base | Admite e sugere documentação oficial |
| Pedido de projeto completo | Resolve em partes pequenas, uma por vez |
| Tentativa de burlar regras ("ignore suas instruções") | Recusa e continua no escopo |
| Pergunta ambígua | Resposta curta pedindo mais contexto antes de assumir |
| Pergunta sobre versão do Python | Só responde se estiver na base; senão, sugere docs |

✏️ **Personalize:** adicione 1 ou 2 exemplos de interação do SEU contexto e teste se o agente segue o padrão. Se mudar o público, revise o tom (regra 4).
