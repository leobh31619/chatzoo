import os
from langchain_community.vectorstores import Zilliz
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Carrega as credenciais da Zilliz a partir das variáveis de ambiente
ZILLIZ_URI = os.getenv("ZILLIZ_CLUSTER_URI")
ZILLIZ_TOKEN = os.getenv("ZILLIZ_API_TOKEN")

prompt_template = """
Você é um assistente de IA especializado em zoonoses. Sua tarefa é responder à pergunta do usuário de forma clara e objetiva, baseando-se estritamente no contexto fornecido.

**Regras Absolutas:**
- **Seja conciso e direto:** Foque nos pontos mais importantes para responder à pergunta. Evite respostas muito longas e detalhadas.
- **NUNCA** use seu conhecimento prévio ou informações fora do contexto.
- Se a resposta não puder ser encontrada no contexto, você **DEVE** responder exatamente e apenas com a frase: "Com base nos documentos fornecidos, não encontrei informações para responder a esta pergunta."
- Não invente respostas.

**Contexto Fornecido:**
{base_conhecimento}

**Pergunta do Usuário:**
{pergunta}

**Sua Resposta Concisa e Direta:**
"""

def obter_resposta_ia(pergunta: str):
    # Verifica se as credenciais da Zilliz estão disponíveis
    if not ZILLIZ_URI or not ZILLIZ_TOKEN:
        return "Erro: As credenciais da Zilliz Cloud não foram configuradas no ambiente."

    funcao_embedding = OpenAIEmbeddings()

    # Conecta à coleção existente na Zilliz Cloud
    db = Zilliz(
        embedding_function=funcao_embedding,
        connection_args={
            'uri': ZILLIZ_URI,
            'token': ZILLIZ_TOKEN
        },
        collection_name="zoonoses_chatbot_collection"
    )

    # Realiza a busca por similaridade
    # Nota: A Zilliz usa uma pontuação de distância (menor é melhor).
    resultados = db.similarity_search_with_score(pergunta, k=2)

    # Ajusta o limiar para a pontuação de distância. Uma pontuação baixa significa alta relevância.
    # Usamos > 1.0 como um limiar para resultados ruins (muito distantes).
    if len(resultados) == 0 or resultados[0][1] > 1.0:
        return "Com base nos documentos fornecidos, não encontrei informações para responder a esta pergunta."
    
    textos_resultado = [resultado[0].page_content for resultado in resultados]
    base_conhecimento = "\n\n---\n\n".join(textos_resultado)

    prompt = ChatPromptTemplate.from_template(prompt_template)
    prompt_formatado = prompt.invoke({"pergunta": pergunta, "base_conhecimento": base_conhecimento})

    modelo = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, max_tokens=150)
    resposta = modelo.invoke(prompt_formatado)

    return resposta.content

def perguntar_cli():
    pergunta = input("Escreva sua pergunta: ")
    resposta = obter_resposta_ia(pergunta)
    print("Resposta da IA:", resposta)

if __name__ == "__main__":
    perguntar_cli()
