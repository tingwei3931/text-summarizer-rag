from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import os 
from langchain_community.vectorstores import FAISS
from faiss import read_index, write_index
from langchain_community.docstore.in_memory import InMemoryDocstore

def load_documents(doc_folder: Path) -> list[str]:
    documents = []
    for filename in doc_folder.iterdir():
        with open(filename, 'r') as file:
            documents.append(file.read())
    return documents

# Split text into chunks 
def split_text(docs: list[str]) -> list[str]:
    chunks = []
    for doc in docs: 
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = splitter.split_text(doc)
        chunks.extend(texts)
    return chunks

# Create the FAISS vector store
async def create_vector_store(text_chunks: list[str], embeddings: OpenAIEmbeddings):
    vector_store = await FAISS.afrom_texts(text_chunks, embeddings)
    return vector_store

async def initialize_vector_store():
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))
    path_to_docs = Path('data')
    # path_to_vector_store = Path('faiss.index')
    
    docs = load_documents(path_to_docs)
    text_chunks = split_text(docs)
    # if path_to_vector_store.exists():
    #     index = read_index("faiss.index")
    #     vector_store = FAISS(embedding_function=embeddings, index=index, docstore=InMemoryDocstore(), index_to_docstore_id={})
    # else:
    return await create_vector_store(text_chunks, embeddings)
    # write_index(vector_store.index, "faiss.index")
    # return vector_store

if __name__ == '__main__':
    text = load_documents(Path('data/sample.txt'))
    text_chunks = split_text(text)
    vector_store = create_vector_store(text_chunks)
    