"""PyTutor — chat do assistente de estudos de Python.

Rode com: streamlit run src/app.py
Configuração via .env ou variáveis de ambiente: OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL.
"""

import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agente import (  # noqa: E402
    MODELO_PADRAO,
    carregar_base,
    carregar_env,
    montar_cliente,
    montar_system_prompt,
    responder,
)


def main():
    carregar_env()
    st.set_page_config(page_title="PyTutor", page_icon="🐍")
    st.title("🐍 PyTutor — seu assistente de Python")

    base = carregar_base()
    system_prompt = montar_system_prompt(base)

    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    with st.sidebar:
        st.subheader("Tópicos na base")
        for arquivo in base:
            for topico in arquivo.get("topicos", []):
                st.markdown(f"- {topico['titulo']}")
        modelo = st.text_input("Modelo", os.getenv("OPENAI_MODEL", MODELO_PADRAO))
        if st.button("Limpar conversa"):
            st.session_state.mensagens = []
            st.rerun()

    for mensagem in st.session_state.mensagens:
        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

    pergunta = st.chat_input("Pergunte sobre Python...")
    if not pergunta:
        return

    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        try:
            texto = responder(montar_cliente(), modelo, system_prompt, st.session_state.mensagens)
        except Exception as erro:
            texto = (
                "⚠️ Não consegui falar com a LLM. "
                f"Verifique as variáveis OPENAI_API_KEY e OPENAI_BASE_URL.\n\n`{erro}`"
            )
        st.markdown(texto)

    st.session_state.mensagens.append({"role": "assistant", "content": texto})


main()
