import streamlit as st
from main import obter_resposta_ia

st.set_page_config(page_title="Chatbot de Zoonoses", layout="centered")

st.title("🤖 Chatbot sobre Zoonoses")
st.caption("Pergunte ao assistente virtual sobre as informações dos documentos.")

# Inicializa o histórico do chat na sessão
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Em que posso ajudar sobre zoonoses?"}
    ]

# Exibe as mensagens do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de input para a pergunta do usuário
if prompt := st.chat_input("Qual é a sua pergunta?"):
    # Adiciona a mensagem do usuário ao histórico e a exibe
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera e exibe a resposta do assistente
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = obter_resposta_ia(prompt)
            st.markdown(response)
    
    # Adiciona a resposta do assistente ao histórico
    st.session_state.messages.append({"role": "assistant", "content": response})
