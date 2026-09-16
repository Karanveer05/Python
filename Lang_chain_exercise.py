"""

#1
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash",google_api_key=gemini_key)
prompt_template=ChatPromptTemplate.from_messages([("system","You are an experienced Python trainer."),("human","Explain {topic}. Include definition, simple example and one real-world use case.")])
output_parser=StrOutputParser()
pipeline=prompt_template|llm|output_parser
final_result=pipeline.invoke({"topic":"Python generators"})
print(final_result)

#2
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash",google_api_key=gemini_key)
prompt_template=ChatPromptTemplate.from_messages([("system","You are an experienced technical teacher."),("human","Explain {topic} for a {level} learner. Include a simple explanation, one example, 3 key points and 2 practice questions.")])
output_parser=StrOutputParser()
learning_chain=prompt_template|llm|output_parser
topic_inputs=[{"topic":"Machine Learning","level":"beginner"},{"topic":"Python Decorators","level":"intermediate"},{"topic":"REST API","level":"beginner"},{"topic":"Docker","level":"intermediate"}]
results=learning_chain.batch(topic_inputs)
for result in results:
print(result)


#3

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableParallel
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash",google_api_key=gemini_key)
prompt_template=ChatPromptTemplate.from_messages([("system","You are an experienced Python developer."),("human","Explain {topic}")])
output_parser=StrOutputParser()
def normalize_text(text):
    cleaned_text=" ".join(text.strip().split())
    return {"topic":cleaned_text}
text_cleaner=RunnableLambda(normalize_text)
response_chain=prompt_template|llm|output_parser
pipeline=text_cleaner|RunnableParallel(cleaned=RunnableLambda(lambda data:data["topic"]),response=response_chain)
raw_text="EXPLAIN RECURSION IN PYTHON "
result=pipeline.invoke(raw_text)
print(result["cleaned"])
print(result["response"])


#4

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash",google_api_key=gemini_key)
prompt_template=ChatPromptTemplate.from_messages([("system","You are an experienced technical interviewer and teacher."),("human","Explain {topic} in a simple way. Include definition, one example and one interview question.")])
output_parser=StrOutputParser()
technical_chain=prompt_template|llm|output_parser
topics=["REST API","Docker","Git Rebase","SQL Index","Async Programming"]
batch_inputs=[{"topic":topic} for topic in topics]
outputs=technical_chain.batch(batch_inputs)
for topic,output in zip(topics,outputs):
    print(topic)
    print(output)
    
#5

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash",google_api_key=gemini_key)
prompt_template=ChatPromptTemplate.from_messages([("system","You are an experienced technical teacher."),("human","Explain {topic} for a {difficulty} learner.")])
output_parser=StrOutputParser()
tutor_chain=prompt_template|llm|output_parser
while True:
    topic_name=input("Topic: ")
    if topic_name.strip().lower()=="exit":
        break
    difficulty_level=input("Difficulty: ")
    for chunk in tutor_chain.stream({"topic":topic_name,"difficulty":difficulty_level}):
        print(chunk,end="",flush=True)
    print()
    
    
#6
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash",google_api_key=gemini_key)
output_parser=StrOutputParser()
explanation_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced technical teacher."),("human","Explain {topic} in detail.")])
summary_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced summary writer."),("human","Create a short summary from this explanation: {explanation}")])
question_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced technical interviewer."),("human","Generate 5 interview questions from this summary: {summary}")])
explanation_chain=explanation_prompt|llm|output_parser
summary_chain=summary_prompt|llm|output_parser
question_chain=question_prompt|llm|output_parser
pipeline=RunnablePassthrough.assign(explanation=explanation_chain)|RunnablePassthrough.assign(summary=summary_chain)|RunnablePassthrough.assign(interview_questions=question_chain)
result=pipeline.invoke({"topic":"Vector Databases"})
print(result["explanation"])
print(result["summary"])
print(result["interview_questions"])

#7
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash",google_api_key=gemini_key)
output_parser=StrOutputParser()
summary_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced summary writer."),("human","Generate a summary for this article: {article}")])
sentiment_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced sentiment classifier."),("human","Classify the sentiment of this article: {article}")])
keyword_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced keyword generator."),("human","Generate important keywords from this article: {article}")])
title_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced title writer."),("human","Create a suitable title for this article: {article}")])
summary_chain=summary_prompt|llm|output_parser
sentiment_chain=sentiment_prompt|llm|output_parser
keyword_chain=keyword_prompt|llm|output_parser
title_chain=title_prompt|llm|output_parser
analysis_chain=RunnableParallel(summary=summary_chain,sentiment=sentiment_chain,keywords=keyword_chain,title=title_chain)
article_text="Artificial Intelligence is changing businesses. It helps companies automate tasks and improve customer service. However, AI also creates privacy and ethical challenges."
result=analysis_chain.invoke({"article":article_text})
print(result["summary"])
print(result["sentiment"])
print(result["keywords"])
print(result["title"])
"""
#8
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()
gemini_key=os.getenv("GEMINI_API_KEY")
llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash",google_api_key=gemini_key)
output_parser=StrOutputParser()
sentiment_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced sentiment classifier."),("human","Classify the sentiment of this review: {review}")])
problem_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced product problem analyzer."),("human","Extract the problems from this review: {review}")])
positive_prompt=ChatPromptTemplate.from_messages([("system","You are an experienced product feature analyzer."),("human","Extract the positive features from this review: {review}")])
sentiment_chain=sentiment_prompt|llm|output_parser
