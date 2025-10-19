import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Zilliz
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pymilvus import utility # Adicionado

load_dotenv()

PASTA_BASE = "base"

# Get Zilliz credentials from environment variables
ZILLIZ_URI = os.getenv("ZILLIZ_CLUSTER_URI")
ZILLIZ_TOKEN = os.getenv("ZILLIZ_API_TOKEN")

def criar_db():
    # Check if credentials are set
    if not ZILLIZ_URI or not ZILLIZ_TOKEN:
        print("Erro: As variáveis de ambiente ZILLIZ_CLUSTER_URI e ZILLIZ_API_TOKEN não foram definidas no arquivo .env.")
        print("Por favor, adicione-as antes de continuar.")
        return

    print("Carregando documentos da pasta 'base'...")
    documentos = carregar_documentos()
    
    if not documentos:
        print("Nenhum novo documento PDF encontrado na pasta 'base'.")
        return

    print("Dividindo documentos em chunks...")
    chunks = dividir_chunks(documentos)
    
    print("Iniciando a vetorização e o envio para a Zilliz Cloud...")
    vetorizar_chunks(chunks)

def carregar_documentos():
    carregador = PyPDFDirectoryLoader(PASTA_BASE, glob="*.pdf")
    documentos = carregador.load()
    print(f">-> {len(documentos)} documentos carregados.")
    return documentos

def dividir_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )
    chunks = separador_documentos.split_documents(documentos)
    print(f">-> {len(chunks)} chunks criados.")
    return chunks

def vetorizar_chunks(chunks):
    print(">-> Conectando à Zilliz Cloud e verificando a coleção. Isso pode levar alguns minutos...")
    
    collection_name = "zoonoses_chatbot_collection"
    embeddings = OpenAIEmbeddings()
    connection_args = {
        "uri": ZILLIZ_URI,
        "token": ZILLIZ_TOKEN,
    }

    try:
        # Verifica se a coleção já existe
        if utility.has_collection(collection_name, using_alias='default'):
            print(f"Coleção '{collection_name}' já existe. Adicionando novos documentos...")
            # Conecta à coleção existente
            vector_store = Zilliz(
                embedding_function=embeddings,
                collection_name=collection_name,
                connection_args=connection_args,
            )
            # Adiciona os novos documentos
            vector_store.add_documents(chunks)
            print("\n[SUCESSO] Novos documentos adicionados à coleção existente na Zilliz Cloud!")
        else:
            print(f"Coleção '{collection_name}' não encontrada. Criando uma nova coleção...")
            # Cria uma nova coleção com os documentos
            db = Zilliz.from_documents(
                documents=chunks,
                embedding=embeddings,
                connection_args=connection_args,
                collection_name=collection_name,
                auto_id=True
            )
            print("\n[SUCESSO] Banco de Dados criado e populado na Zilliz Cloud!")

    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro ao tentar conectar ou enviar dados para a Zilliz Cloud.")
        print(f"Detalhes do erro: {e}")
        print("\nPor favor, verifique se suas credenciais no arquivo .env estão corretas e se o cluster da Zilliz está ativo.")


if __name__ == "__main__":
    criar_db()