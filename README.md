# InfoSUS - Chatbot sobre Zoonoses

Um chatbot inteligente desenvolvido com Python, LangChain e Streamlit para responder perguntas sobre zoonoses baseado em documentos especializados.

## 🚀 Funcionalidades

- **Interface Web Intuitiva**: Interface moderna desenvolvida com Streamlit
- **IA Avançada**: Utiliza GPT-4o-mini da OpenAI para respostas precisas
- **Busca Vetorial**: Sistema de busca semântica com Zilliz Cloud
- **Base de Conhecimento**: Documentos especializados sobre zoonoses e saúde pública
- **Respostas Contextuais**: Respostas baseadas exclusivamente nos documentos fornecidos

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Streamlit** - Interface web
- **LangChain** - Framework de IA
- **OpenAI GPT-4o-mini** - Modelo de linguagem
- **Zilliz Cloud** - Banco de dados vetorial
- **pymilvus** - Cliente para Zilliz

## 📋 Pré-requisitos

- Python 3.8+
- Conta na OpenAI
- Conta na Zilliz Cloud
- Git

## 🔧 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/chatzoo-clean.git
cd chatzoo-clean
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r drive/requirements.txt
```

4. **Configure as variáveis de ambiente:**
   - Copie o arquivo `env.example` para `.env`
   - Preencha com suas credenciais:
```env
ZILLIZ_CLUSTER_URI=sua_uri_do_zilliz
ZILLIZ_API_TOKEN=seu_token_do_zilliz
OPENAI_API_KEY=sua_chave_da_openai
```

## 🚀 Como Executar

1. **Execute o aplicativo Streamlit:**
```bash
streamlit run drive/app.py
```

2. **Acesse no navegador:**
   - Abra http://localhost:8501
   - Faça suas perguntas sobre zoonoses

## 📁 Estrutura do Projeto

```
chatzoo-clean/
├── base/                    # Documentos PDF sobre zoonoses
├── drive/                   # Código principal
│   ├── app.py              # Interface Streamlit
│   ├── main.py             # Lógica do chatbot
│   ├── requirements.txt    # Dependências Python
│   └── criar_db.py         # Script para criar base de dados
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Este arquivo
```

## 🔐 Configuração da Base de Dados

O chatbot utiliza a Zilliz Cloud para armazenar e buscar informações dos documentos. Certifique-se de:

1. Criar uma conta na [Zilliz Cloud](https://zilliz.com/)
2. Criar um cluster
3. Obter a URI e o token de API
4. Configurar as variáveis de ambiente

## 📚 Documentos Incluídos

O chatbot possui acesso aos seguintes documentos sobre zoonoses:
- Capítulos sobre zoonoses (1-4)
- E-books sobre processo saúde-doença
- Materiais do SUS e PNAD
- Vídeos educativos

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas, abra uma issue no repositório.

---

**Desenvolvido com ❤️ para promover conhecimento sobre zoonoses e saúde pública**
