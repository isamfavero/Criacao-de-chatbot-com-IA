

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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")

st.write("### ChatBot com IA") 

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o")
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


