import sys
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Carrega as variáveis de ambiente (necessário para a chave da OpenAI)
load_dotenv()

CAMINHO_DB = "db"

def depurar_busca(pergunta: str):
    """
    Executa a mesma busca de similaridade que o chatbot e imprime os resultados.
    """
    print(f"--- Depurando a busca para a pergunta: '{pergunta}' ---\n")
    
    try:
        funcao_embedding = OpenAIEmbeddings()
        db = Chroma(persist_directory=CAMINHO_DB, embedding_function=funcao_embedding)
        
        print("Base de dados Chroma carregada com sucesso.")
        
        resultados = db.similarity_search_with_relevance_scores(pergunta, k=4)
        
        if len(resultados) == 0:
            print("\n--- Nenhum resultado encontrado na base de dados. ---")
            return

        print(f"\n--- {len(resultados)} resultados encontrados: ---\n")
        
        for i, (doc, score) in enumerate(resultados):
            print(f"--- Resultado {i+1} | Pontuação de Relevância: {score:.4f} ---")
            print(doc.page_content)
            print("-" * 50)
            
    except Exception as e:
        print(f"\n--- Ocorreu um erro ao tentar acessar ou buscar na base de dados: ---")
        print(e)
        print("\nIsso pode indicar um problema com a base de dados (pode estar corrompida ou vazia) ou com a configuração.")

if __name__ == "__main__":
    # Pega a pergunta dos argumentos da linha de comando
    if len(sys.argv) > 1:
        pergunta_usuario = " ".join(sys.argv[1:])
        depurar_busca(pergunta_usuario)
    else:
        print("Por favor, forneça uma pergunta como argumento. Ex: python debug_retrieval.py sua pergunta aqui")
