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