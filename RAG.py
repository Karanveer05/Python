#1

retriever=vectorstore.as_retriever(search_kwargs={"k":5})
def is_relevant(question,doc):
    question_words=set(question.lower().split())
    content_words=set(doc.page_content.lower().split())
    return len(question_words.intersection(content_words))>0
def remove_duplicates(docs):
    seen=set()
    unique_docs=[]
    for doc in docs:
        content=doc.page_content.strip()
        if content not in seen:
            unique_docs.append(doc)
            seen.add(content)
    return unique_docs
def format_docs(docs):
    seen=set()
    filtered_docs=[]
    for doc in docs:
        content=doc.page_content.strip()
        if content not in seen:
            filtered_docs.append(doc)
            seen.add(content)
    return "\n\n".join(doc.page_content for doc in filtered_docs)
question=input("Ask a question about the PDF: ")
retrieved_docs=retriever.invoke(question)
print("\nRetrieved Chunks")
for i,doc in enumerate(retrieved_docs,1):
    print(f"\nChunk {i}")
    print("Source:",doc.metadata)
    print("Content:")
    print(doc.page_content)
relevant_docs=[]
for doc in retrieved_docs:
    if is_relevant(question,doc):
        relevant_docs.append(doc)
filtered_docs=remove_duplicates(relevant_docs)
print("\nFiltered Chunks")
for i,doc in enumerate(filtered_docs,1):
    print(f"\nChunk {i}")
    print("Source:",doc.metadata)
    print("Content:")
    print(doc.page_content)
final_docs=filtered_docs[:3]
print("\nFinal Top-3 Context")
for i,doc in enumerate(final_docs,1):
    print(f"\nChunk {i}")
    print(doc.page_content)
context=format_docs(final_docs)
prompt=f"""Answer the question only from the given context.
Context:
{context}
Question:
{question}
Answer:"""
answer=llm.invoke(prompt)
print("\nLLM Answer")
print(answer.content if hasattr(answer,"content") else answer)


#2

from langchain_core.documents import Document
docs=[
Document(page_content="Employees must provide 30 days notice.",metadata={"source":"notice_policy.pdf"}),
Document(page_content="Employees must provide 30 days notice.",metadata={"source":"notice_policy.pdf"}),
Document(page_content="The employee notice period is 30 days.",metadata={"source":"notice_policy.pdf"}),
Document(page_content="Employees are required to give 30 days notice.",metadata={"source":"resignation_policy.pdf"}),
Document(page_content="Employees must provide 30 days notice.",metadata={"source":"notice_policy.pdf"})
]
def format_docs(docs):
    seen=set()
    filtered_docs=[]
    print("Chunks before duplicate removal:",len(docs))
    for doc in docs:
        content=doc.page_content.strip()
        if content not in seen:
            filtered_docs.append(doc)
            seen.add(content)
    print("Chunks after duplicate removal:",len(filtered_docs))
    return "\n\n".join(doc.page_content for doc in filtered_docs)
print("\nRetrieved Chunks")
for i,doc in enumerate(docs,1):
    print(f"\nChunk {i}")
    print(doc.page_content)
context=format_docs(docs)
print("\nFormatted Context")
print(context)


#3

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
loader=PyPDFLoader("company_hr_policy.pdf")
documents=loader.load()
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks=text_splitter.split_documents(documents)
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore=FAISS.from_documents(chunks,embeddings)
retriever=vectorstore.as_retriever(search_kwargs={"k":3})
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.getenv("GEMINI_API_KEY"))
def format_docs(docs):
    seen=set()
    filtered_docs=[]
    for doc in docs:
        content=doc.page_content.strip()
        if content not in seen:
            filtered_docs.append(doc)
            seen.add(content)
    return "\n\n".join(doc.page_content for doc in filtered_docs)
def run_rag(question):
    docs=retriever.invoke(question)
    context=format_docs(docs)
    prompt=f"""Answer the question using only the given context.
Context:
{context}
Question:
{question}
Answer:"""
    answer=llm.invoke(prompt)
    return answer.content
response_cache={}
def ask_question(question):
    normalized_question=question.strip().lower()
    if normalized_question in response_cache:
        print("\nCache Hit")
        return response_cache[normalized_question]
    print("\nCache Miss")
    answer=run_rag(normalized_question)
    response_cache[normalized_question]=answer
    return answer
while True:
    question=input("\nAsk a question about the PDF or type exit: ")
    if question.strip().lower()=="exit":
        break
    answer=ask_question(question)
    print("\nAnswer:")
    print(answer)
    
    
    #4
    
    import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
documents=[]
base_path="company_corpus"
for department in os.listdir(base_path):
    department_path=os.path.join(base_path,department)
    if not os.path.isdir(department_path):
        continue
    for filename in os.listdir(department_path):
        if filename.lower().endswith(".pdf"):
            file_path=os.path.join(department_path,filename)
            loader=PyPDFLoader(file_path)
            docs=loader.load()
            for doc in docs:
                doc.metadata["department"]=department
                doc.metadata["source_file"]=filename
                doc.metadata["version"]="2026"
            documents.extend(docs)
print("\nTotal documents/pages:",len(documents))
text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
chunks=text_splitter.split_documents(documents)
print("Total chunks:",len(chunks))
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore=FAISS.from_documents(chunks,embeddings)
retriever=vectorstore.as_retriever(search_kwargs={"k":5})
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.getenv("GEMINI_API_KEY"))
def format_docs(docs):
    seen=set()
    filtered_docs=[]
    for doc in docs:
        content=doc.page_content.strip()
        if content not in seen:
            filtered_docs.append(doc)
            seen.add(content)
    return "\n\n".join(doc.page_content for doc in filtered_docs)
question=input("\nAsk a question about company policies: ")
retrieved_docs=retriever.invoke(question)
print("\nRetrieved Chunks")
for i,doc in enumerate(retrieved_docs,1):
    print(f"\nChunk {i}")
    print("Department:",doc.metadata.get("department"))
    print("Source File:",doc.metadata.get("source_file"))
    print("Version:",doc.metadata.get("version"))
    print("Page:",doc.metadata.get("page"))
    print("Content:")
    print(doc.page_content)
context=format_docs(retrieved_docs)
prompt=f"""Answer the question using only the company documents given below.
Context:
{context}
Question:
{question}
Answer:"""
answer=llm.invoke(prompt)
print("\nLLM Answer:")
print(answer.content)