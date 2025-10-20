import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Zilliz
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pymilvus import utility, connections

load_dotenv()

PASTA_BASE = "../base"

# Get Zilliz credentials from environment variables
ZILLIZ_URI = os.getenv("ZILLIZ_CLUSTER_URI")
ZILLIZ_TOKEN = os.getenv("ZILLIZ_API_TOKEN")

def criar_db():
    if not ZILLIZ_URI or not ZILLIZ_TOKEN:
        print("Erro: As variáveis de ambiente ZILLIZ_CLUSTER_URI e ZILLIZ_API_TOKEN não foram definidas.")
        return

    print("Carregando e limpando metadados dos documentos...")
    documentos = carregar_e_limpar_documentos()
    
    if not documentos:
        print("Nenhum documento PDF encontrado na pasta 'base'.")
        return

    print("Dividindo documentos em chunks...")
    chunks = dividir_chunks(documentos)
    
    print("Iniciando a vetorização e o envio para a Zilliz Cloud...")
    vetorizar_chunks(chunks)

def carregar_e_limpar_documentos():
    carregador = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = carregador.load()
    
    if not documentos:
        return []

    print("Padronizando metadados para garantir consistência...")
    for doc in documentos:
        doc.metadata = {
            "source": doc.metadata.get("source", "N/A"),
            "page": doc.metadata.get("page", 0)
        }
    
    nomes_arquivos = list(set([os.path.basename(doc.metadata.get('source', 'N/A')) for doc in documentos]))
    print(f">-> Arquivos PDF processados: {nomes_arquivos}")
    print(f">-> {len(documentos)} páginas de documentos carregadas e limpas.")
    return documentos

def dividir_chunks(documentos):
    separador = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
    chunks = separador.split_documents(documentos)
    print(f">-> Documentos divididos em {len(chunks)} chunks.")
    return chunks

def vetorizar_chunks(chunks):
    print(">-> Conectando à Zilliz Cloud...")
    
    collection_name = "zoonoses_chatbot_collection"
    embeddings = OpenAIEmbeddings()
    alias = "default"
    
    connection_args = {
        "uri": ZILLIZ_URI,
        "token": ZILLIZ_TOKEN,
    }

    try:
        print(f"Estabelecendo conexão com o alias '{alias}'...")
        connections.connect(alias=alias, **connection_args)
        print("Conexão estabelecida.")

        if utility.has_collection(collection_name):
            print(f"Coleção '{collection_name}' já existe. Apagando-a para recriar do zero...")
            utility.drop_collection(collection_name)
            print("Coleção apagada com sucesso.")

        print(f"Criando nova coleção '{collection_name}' com {len(chunks)} chunks...")
        Zilliz.from_documents(
            documents=chunks,
            embedding=embeddings,
            connection_args=connection_args,
            collection_name=collection_name,
            auto_id=True
        )
        print("\n[SUCESSO] Nova coleção criada e populada na Zilliz Cloud!")

    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro inesperado durante o processo.")
        print(f"Detalhes do erro: {e}")
    finally:
        try:
            if connections.has_connection(alias):
                print(f"Fechando a conexão com o alias '{alias}'...")
                connections.disconnect(alias)
                print("Conexão fechada.")
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")

if __name__ == "__main__":
    criar_db()