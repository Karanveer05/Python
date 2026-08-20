""""

#1
from transformers import pipeline
text=str(input("Enter text: ")).lower()
while(text!="exit"):
    classifier=pipeline("sentiment-analysis")
    result=classifier(text)
    print(f"Sentiment  : {result[0]['label']}")
    print(f"Confidence : {result[0]['score']}")
print("Sucessfully Exit the Program")

# 2
from transformers import pipeline
classifier=pipeline("sentiment-analysis")
texts=[
    "I love this product.",
    "This product is terrible.",
    "The experience was okay."
]
results=classifier(texts)
for i,result in enumerate(results,start=1):
  print(f"Review {1}---{result['label']}--{result['score']}")

# 3

from transformers import pipeline
prompt=str(input("Enter Prompt : ")).lower
while(prompt!="exit"):
    Generator=pipeline("text-generation")
    Result=Generator(prompt, max_length=50,num_return_sequences=1)
    print(f"Generated :\n{Result[0]['generated_text']}")

# 4
from transformers import pipeline
number=0
def display():
    print("-"*50)
    print("1. Sentiment Analysis\n2. Text Generation\n3.Exit")
    Number=int(input("Enter your Choice ( 1 or 2 or 3 ) : "))
    global number
    number=Number
    switch_case()

def text_generation():
    print("-"*50)
    prompt=str(input("Enter Prompt : "))
    Genarator=pipeline("text-generation")
    Result=Genarator(prompt,max_length=50,num_return_sequences=1)
    print(f"Generated :\n{Result[0]['generated_text']}")
    display()
    
    
def Sentiment_Analysis():
    print("-"*50)
    text=str(input("Enter text: ")).lower()
    classifier=pipeline("sentiment-analysis")
    result=classifier(text)
    print(f"Sentiment  : {result[0]['label']}")
    print(f"Confidence : {result[0]['score']}")
    display()
        
def switch_case():
    match number:
        case 1:
            Sentiment_Analysis()
        case 2:
            text_generation()
        case 3:
            return
        case _:
            print("invalid option")
            display()
display()
    


# 5
from nltk.tokenize import sent_tokenize 
from transformers import pipeline
import nltk
# nltk.download("punkt")
# nltk.download("punkt_tab")
import pandas as pd
sum_of_scores=0
Review_positive=0
classifier=pipeline("sentiment-analysis")
Input=str(input("Enter the statements (eg he is best. i am good) : "))
Input_list=sent_tokenize(Input)
results=classifier(Input_list)
for i,result in enumerate(results,start=0):
    print("-"*35)
    print(Input_list[i])
    sum_of_scores=sum_of_scores+result['score']
    print(f"{result['label']}  |  {result['score']}\n")
print("-"*35)
print(f"Total Reviews : {len(Input_list)}")
for result in results:
    if result['label']=='POSITIVE':
        Review_positive=Review_positive+1
print(f"Positive : {Review_positive}")
print(f"Negative : {len(Input_list)-Review_positive}")
print(f"Average confidence : {sum_of_scores/len(Input_list)}")

# 6

from transformers import pipeline
number=0
def display():
    print("-"*50)
    print("1. Blog Introduction\n2. Product Description\n3. Social Media Post\n4.Exit")
    Number=int(input("Enter your Choice ( 1-4 ) : "))
    global number
    number=Number
    switch_case()

def text_generation(prompt):
    topic=str(input("Enter the Topic : "))
    complete_prompt = (
    prompt + topic +
    ". Start directly with the content. "
    "Do not repeat the instruction."
    )
    Genarator=pipeline("text-generation",model="Qwen/Qwen2.5-0.5B-Instruct")
    Result=Genarator(complete_prompt,max_length=50,num_return_sequences=2,return_full_text=False)
    print("-"*50)
    print(f"Generated :\n{Result[0]['generated_text']}")
    display()
    
    

        
def switch_case():
    match number:
        case 1:
            text_generation("Write the blog on ")
        case 2:
            text_generation("Write Product Description on ")
        case 3:
            text_generation("Write about  Social Media Post of ")
        case 4:
            print("Exit Sucessfully")
            return
        case _:
            print("Invalid Option ")
            display()
display()


# 7

from transformers import pipeline
classifier = pipeline("sentiment-analysis")
user_text = __builtins__.input("Enter the text : ")
result = classifier(user_text)
print(f"Input : {user_text}")
print(f"Sentiment : {result[0]['label']}")
prompt = (f"
You are a professional customer service representative.

Your task is to reply to the customer's review below.

Instructions:
- Respond as the company/customer support representative.
- Be polite, professional, and helpful.
- Keep the response short, around 2-4 sentences.
- If the customer is unhappy, apologize and offer help or a solution.
- If the customer is happy, thank them and show appreciation.
- Do not repeat or summarize the customer's review.
- Do not mention that you are an AI.
- Do not explain what you are doing.
- Start directly with the customer service response.
- Return only the response.

Customer review:
{user_text}

Customer service response:
")
response_generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)
respond = response_generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1,
    return_full_text=False
)
print(f"Generated Response : {respond[0]['generated_text']}")


"""

#8
from transformers import pipeline
from nltk.tokenize import sent_tokenize
number=0

def Analyze_Multiple_Reviews():
    sum_of_scores=0
    Review_positive=0
    classifier=pipeline("sentiment-analysis")
    Input=str(input("Enter the statements (eg he is best. i am good) : "))
    Input_list=sent_tokenize(Input)
    results=classifier(Input_list)
    for i,result in enumerate(results,start=0):
        print("-"*35)
        print(Input_list[i])
        sum_of_scores=sum_of_scores+result['score']
        print(f"{result['label']}  |  {result['score']}\n")
    print("-"*35)
    print(f"Total Reviews : {len(Input_list)}")
    for result in results:
        if result['label']=='POSITIVE':
            Review_positive=Review_positive+1
    print(f"Positive : {Review_positive}")
    print(f"Negative : {len(Input_list)-Review_positive}")
    print(f"Average confidence : {sum_of_scores/len(Input_list)}")
    display()
    
    
def display():
    print("-"*50)
    print("\t\tAI ASSISTANT")
    print("="*50)
    print("1. Analyze Sentiment\n2. Generate Text\n3. Analyze Multiple Reviews\n4.Exit")
    Number=int(input("Enter your Choice ( 1-4 ) : "))
    global number
    number=Number
    switch_case()


def Sentiment_Analysis():
    print("-"*50)
    text=str(input("Enter text: ")).lower()
    classifier=pipeline("sentiment-analysis")
    result=classifier(text)
    print(f"Sentiment  : {result[0]['label']}")
    # print(f"Confidence : {result[0]['score']}")
    display()
    
    
def text_generation(prompt):
    topic=str(input("Enter the Topic : "))
    complete_prompt = (
    prompt + topic +
    ". Start directly with the content. "
    "Do not repeat the instruction."
    )
    Genarator=pipeline("text-generation",model="Qwen/Qwen2.5-0.5B-Instruct")
    Result=Genarator(complete_prompt,max_length=50,num_return_sequences=2,return_full_text=False)
    print("-"*50)
    print(f"Generated :\n{Result[0]['generated_text']}")
    display()
    
    

        
def switch_case():
    match number:
        case 1:
            Sentiment_Analysis()
        case 2:
            text_generation()
        case 3:
            text_generation()
        case 4:
            print("Exit Sucessfully")
            return
        case _:
            print("Invalid Option ")
            display()
display()

