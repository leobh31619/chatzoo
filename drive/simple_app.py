import streamlit as st

# Configuração básica
st.set_page_config(
    page_title="InfoSUS - Teste Simples", 
    layout="wide", 
    page_icon="🤖"
)

# Título simples
st.title("🤖 InfoSUS - Chatbot de Zoonoses")
st.subheader("Assistente Virtual Especializado em Zoonoses e Saúde Pública")

# Teste de cores
st.success("✅ Interface funcionando!")
st.info("ℹ️ Se você vê esta mensagem, o Streamlit está carregando.")

# Teste de layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💬 Chat")
    st.write("Área do chat aqui")

with col2:
    st.markdown("### 📋 Informações")
    st.write("Sidebar com informações")

# Teste de CSS simples
st.markdown("""
<style>
    .test-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1e3c72;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="test-box">
    <h3>🎨 Teste de CSS</h3>
    <p>Se você vê esta caixa com borda azul, o CSS está funcionando!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.write("**Status:** Interface carregada com sucesso! 🎉")
