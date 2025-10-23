import streamlit as st
import os
from main import obter_resposta_ia

# Configuração da página
st.set_page_config(
    page_title="InfoSUS - Chatbot de Zoonoses", 
    layout="wide", 
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# CSS personalizado para melhorar o visual
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .main-title {
        color: white;
        font-size: 3rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .main-subtitle {
        color: #e8f4fd;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        font-weight: 300;
    }
    
    .chat-container {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
    }
    
    .sidebar-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    
    .feature-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2a5298;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stChatMessage {
        background-color: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1 class="main-title">🤖 InfoSUS</h1>
    <p class="main-subtitle">Assistente Virtual Especializado em Zoonoses e Saúde Pública</p>
</div>
""", unsafe_allow_html=True)

# Layout em duas colunas
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 💬 Chat com o Assistente")
    st.markdown("Faça suas perguntas sobre zoonoses, saúde pública e informações do SUS.")

# Sidebar com informações
with col2:
    st.markdown("""
    <div class="sidebar-info">
        <h3>📋 Sobre o InfoSUS</h3>
        <p>Assistente virtual especializado em zoonoses e saúde pública, desenvolvido com IA avançada.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Funcionalidades")
    st.markdown("""
    <div class="feature-card">
        <strong>🔍 Busca Inteligente</strong><br>
        Encontre informações precisas nos documentos
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <strong>📚 Base de Conhecimento</strong><br>
        Documentos especializados em zoonoses
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <strong>🤖 IA Avançada</strong><br>
        Respostas baseadas em GPT-4o-mini
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📖 Documentos Disponíveis")
    st.markdown("""
    - 📄 Capítulos sobre Zoonoses (1-4)
    - 📚 E-books de Saúde Pública
    - 🏥 Materiais do SUS
    - 📊 Dados da PNAD
    - 🎥 Vídeos Educativos
    """)
    
    st.markdown("### 💡 Dicas de Uso")
    st.markdown("""
    - Seja específico em suas perguntas
    - Use termos técnicos quando souber
    - Peça exemplos quando necessário
    - O assistente responde apenas com base nos documentos
    """)

# Container do chat
with col1:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Inicializa o histórico do chat na sessão
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "👋 Olá! Sou o InfoSUS, seu assistente virtual especializado em zoonoses e saúde pública. Em que posso ajudar você hoje?"}
        ]

    # Exibe as mensagens do histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Campo de input para a pergunta do usuário
    if prompt := st.chat_input("💬 Digite sua pergunta sobre zoonoses ou saúde pública..."):
        # Adiciona a mensagem do usuário ao histórico e a exibe
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gera e exibe a resposta do assistente
        with st.chat_message("assistant"):
            with st.spinner("🔍 Analisando documentos e preparando resposta..."):
                response = obter_resposta_ia(prompt)
                st.markdown(response)
        
        # Adiciona a resposta do assistente ao histórico
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🤖 <strong>InfoSUS</strong> - Assistente Virtual de Zoonoses | Desenvolvido com Python, LangChain e Streamlit</p>
    <p>💡 Para melhor experiência, use perguntas específicas e detalhadas</p>
</div>
""", unsafe_allow_html=True)