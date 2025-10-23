# Script para iniciar o chatbot InfoSUS
Write-Host "🤖 Iniciando InfoSUS Chatbot..." -ForegroundColor Green

# Navegar para a pasta drive
Set-Location "C:\Users\leona\Desktop\Curso#\chatzoo-clean\drive"

# Verificar se o arquivo existe
if (Test-Path "app.py") {
    Write-Host "✅ Arquivo app.py encontrado" -ForegroundColor Green
    
    # Limpar cache do Streamlit
    Write-Host "🧹 Limpando cache do Streamlit..." -ForegroundColor Yellow
    streamlit cache clear
    
    # Iniciar o Streamlit
    Write-Host "🚀 Iniciando servidor Streamlit..." -ForegroundColor Cyan
    Write-Host "📱 Acesse: http://localhost:8501" -ForegroundColor Magenta
    Write-Host "⏹️  Para parar: Ctrl+C" -ForegroundColor Red
    
    # Executar o Streamlit
    streamlit run app.py --server.runOnSave true
} else {
    Write-Host "❌ Arquivo app.py não encontrado!" -ForegroundColor Red
    Write-Host "📁 Diretório atual: $(Get-Location)" -ForegroundColor Yellow
    Write-Host "📋 Arquivos disponíveis:" -ForegroundColor Yellow
    Get-ChildItem
}
