from langchain_openai import ChatOpenAI
import os 
# from langchain import hub
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import asyncio

def create_rag_pipeline(vector_store):
    # Init LLM model 
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv('OPENAI_API_KEY'))
    
    # Define a prompt for summarization
    template = """
    Given the following pieces of context, write a concise summary based on the question:
    {context}
    
    Question: {input}
    """
    
    # retriever = vector_store.as_retriever()
    # retrieval_template = """
    # Retrieve relevant information based on the following query and context:
    # <context>
    # {context}
    # </context>
    # Question: {input}
    # """
    # retrieval_prompt = ChatPromptTemplate([retrieval_template])
    # document_chain = create_stuff_documents_chain(llm, retrieval_prompt)
    # # Create the RAG chain: Retrieval -> Generation
    # retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # Retrieve and generate using relevant snippets of the blog. 
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    
    # Takes in the key "context" and "question"
    # custom_rag_prompt = PromptTemplate.from_template(template)
    
    # LCEL: 
    # retriever | format_docs passes the question through the retriever, generating docs,
    # and then formats the docs to generate a string.
    # RunnablePassthrough() is a placeholder that passes the question through unchanged.
    # StrOutputParser simply extracts the "answer" key from the llm output.
    # rag_chain = (
    #     {"context": retriever | format_docs, "question": RunnablePassthrough()}
    #     | prompt
    #     | llm
    #     | StrOutputParser()
    # )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            ("human", "{input}")
        ]
    )
    
    summarization_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, summarization_chain)
    return rag_chain

 
def summarize_with_rag(query, vector_store):
    rag_chain = create_rag_pipeline(vector_store)
    response = rag_chain.invoke({'input': query})
    return response["answer"]


