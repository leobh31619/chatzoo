import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="InfoSUS - Teste", 
    layout="wide", 
    page_icon="🤖"
)

# Teste simples
st.title("🤖 InfoSUS - Teste de Interface")
st.write("Se você está vendo esta mensagem, o Streamlit está funcionando!")

# Teste de CSS
st.markdown("""
<style>
    .test-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="test-header">
    <h1>Teste de CSS Funcionando!</h1>
    <p>Se você vê este gradiente azul, o CSS está sendo aplicado corretamente.</p>
</div>
""", unsafe_allow_html=True)

st.success("✅ Interface funcionando!")
st.info("ℹ️ Se você vê esta mensagem colorida, o Streamlit está carregando corretamente.")
