"""

# 1
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)
response=client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what Artificial Intelligence is in simple words"
)
print("output :\n",response.text)


#2

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

user_input=str(input("Enter the content "))

client = genai.Client(api_key=api_key)
response=client.models.generate_content(
    model="gemini-3.6-flash",
    contents=user_input
)

print(response.text)


# 3 
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

def llm(prompt):
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return(response.text)

def display():
    prompt_1=str(input("Enter the Prompt 1 :"))
    prompt_2=str(input("Enter the Prompt 2 :"))
    prompt_3=str(input("Enter the Prompt 3 :"))
    print("-"*50)
    print(f"\nPrompt 1 : {prompt_1} \n{llm(prompt_1)}")
    print("-"*50)
    print(f"\nPrompt 2 : {prompt_2} \n{llm(prompt_2)}")
    print("-"*50)
    print(f"\nPrompt 3 : {prompt_3} \n{llm(prompt_3)}")

display()


# 4
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

user_input=input("Enter the content That you want to summarize :\n")

response=client.models.generate_content(
    model="gemini-3.6-flash",
    contents=user_input + "\nSummarize the above content in 2-3 lines "
)

print(response.text)



# 5

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
def llm_model(content,language):
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=content +"\n only display it in " +language
    )
    return(response.text)
content=input("Enter the text :")
language=input("Enter the language you want to convert it in :")
print("-"*50)
print("converted text is :\n\n",llm_model(content,language))


#6

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

system_instructions=""You are a Python tutor. Explain programming concepts in simple language and always provide a small example
Ask the user 3 different Python questions and observe how the system instruction affects the responses
""

def llm_model(prompt):
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents= prompt,
        config={"system_instruction":system_instructions}
    )
    return (response.text)
prompt_list=[]
for i in range(1,4):
    print("-"*50)
    text=input(f"Enter your instruction {i} :")
    prompt_list.append(text)
    
for i in range(0,len(prompt_list)):
    print("--"*30)
    print(f"Question : {prompt_list[i]} \n\n{llm_model(prompt_list[i])}")
    

# 7
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

system_instructions=""You are a Python tutor. Explain programming concepts in simple language 
the user give u a code  Explain what the code does. Identify the important concepts used.
Explain the code step-by-step.

""
def llm_model(content):
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=content,
        config={
            "system_instruction":system_instructions
            }
    )
    return(response.text)
code_line_list=[]
print("-"*50)
print("Enter the python code here :\n\n")
while True:
    line=input()
    if line.strip().lower()=="end":
        break
    code_line_list.append(line)
content="\n".join(code_line_list)
print("--"*30)

print("\n",llm_model(content))


# 8 

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
try:
    api_key=os.getenv("GEMINIAPI_KEY")
    client=genai.Client(api_key=api_key)
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Explain what Artificial Intelligence is in simple words"
    )
    print("output :\n",response.text)  
except Exception as error:
    print("API not found")  


# 9
 
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


def model_llm(prompt):
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "system_instruction":""you have to answer to the point. your answer is suffcient and minimum""
        }
    )
    return(response.text)
print("Ai assistant is ready to conversation")
while True:
    line=input("\nYOU :")
    if  line.strip().lower()=="exit":
        print("Assistant : EThanks for your conversation")
        break
    print("Assistant : ",model_llm(line))


# 10 

 
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


def model_llm(prompt):
    conversation=""
    for message in history:
     conversation += (
        message["role"]+":"+message["content"]+"\n"
     )
    conversation +="user:"+prompt 
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=conversation,
        config={
            "system_instruction":""Answer clearly and to the point.Remember relevant information from the conversation history.""
        }
    )
    return(response.text)
print("Ai assistant is ready to conversation")
history=[]
while True:
    
    line=input("\nYOU :")
    if  line.strip().lower()=="exit":
        print("Assistant : Thanks for your conversation")
        break
    response=model_llm(line)
    print("Assistant : ",response)
    history.append({
        "role":"user",
        "content":line
        })
    history.append({
        "role":"assistant",
        "content":response
    })


# 11

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)
history=[]
def model_llm(prompt):
    conversation=""
    for message in history:
        conversation += message["role"]+":"+message["content"]+"\n"
    conversation += prompt
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=conversation,
        config={
            "system_instruction":""
            You are a professional technical interviewer.
            Ask the user one Python interview question at a time.
            Wait for the user's answer.
            Evaluate the answer.
            Give short feedback.
            Then ask the next Python question.
            ""
            
        }
    )
    return(response.text)
print("-"*50)
history=[]
print("Now Ai Assistant is ready to ask question ")
print("type -- (exit) to end this)")
line="ask me question now"
while line.strip().lower()!="exit":
    response=model_llm(line)
    print(response)
    line=input("ANSWER : ")
    history.append({
        "role":"user",
        "content":line
    })
    
    history.append({
        "role":"Assistant",
        "content":response
    })
    


# 12
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
count=1
def display():
    global count
    try:
        api_key=os.getenv("GEMINIAPI_KEY")
        client=genai.Client(api_key=api_key)
        response=client.models.generate_content(
            model="gemini-3.6",
            contents="Explain what Artificial Intelligence is in simple words"
        )
        print("output :\n",response.text)  
    except Exception as error:
        if count<4:
            print(f"Attempt {count} failed")  
            count +=1
            print("Retrying...")  
            display()
        else:
            print("----------Unable to get a response------------")
            return 
display()


# 13
import json
import os
import time
from google import genai
from dotenv import load_dotenv
load_dotenv()
def previous_content():
    
    content=""
    with open("history.jsonl","r") as file:
     for line in file:
        line = line.strip()
        if line == "":
            continue
        message=json.loads(line)
        if message["content"] is None:
         content += f"{message['role']} : Error Api Request Failed \n"
        else:
         content += f"{message['role']} : {message['content']} \n"
        
        if message["role"]=="Assistant":
            content+="\n"

    return content

      
count=1      
def Api_key(input_data):

    global count
    history=previous_content()
    try:
        
        api_key=os.getenv("GEMINI_API_KEY")
        client=genai.Client(api_key=api_key)
        data=history +"\n\n"+input_data
        response=client.models.generate_content(
            model="gemini-3.6-flash", # correct it run the program
            contents=data,
            config={
                "system_instruction":"you have to answer to the point make it simple and minimum and above is previous history used the history to give relevant info also rember previous history if ask any previous question also give greeting to person ask for what u can help at first question if nesscary "
            }
            )
        # print("output :\n",response.txt) 
        return response.text
    except Exception as error:
         if count<4:
            print(f"Attempt {count} failed")  
            count +=1
            print("Retrying...") 
            time.sleep(3) 
            return Api_key(input_data)
         else:
             print("Error :API Request failed")
             return False
def display(): 
    global count
    print("-"*50)
    print("Program Started")
    time.sleep(3)
    print("-"*50)
    print("User logged in ")
    if previous_content() is not None:
        print("File Loaded Sucessfully")
    print("-"*50)
    print("Checking API Request :")
    time.sleep(3)

    if Api_key("a") is False:
        return
    else:
        print("API Connection Build Sucessfully")
    print("-"*50)
    data=input("ENTER THE TEXT : ")
    while data.strip().lower()!="exit":
        result=Api_key(data)
        if result!=None:
         print(result)
        if os.path.exists("history.jsonl"):
         with open("history.jsonl","a") as file:
          json.dump({
            "role":"user",
            "content":data
            },file)
          file.write("\n")
          json.dump({
            "role":"Assistant",
            "content":result
             },file)
          file.write("\n")

        print("-"*50)
        data=input("ENTER THE TEXT : ")
        count=1
    print("-"*50)
    print("\nThanks for your conversation\n")
    print("Python Program Stopped\n")
display()

# 14

import json
import os
import time
from google import genai
from dotenv import load_dotenv
load_dotenv()
def previous_content():
    
    content=""
    with open("orders.jsonl","r") as file:                                                                                               
     for line in file:
        line = line.strip()
        if line == "":
            continue
        message=json.loads(line)
        content += f"{message['order']} : {message['price']} \n"
        content+="\n\n"
    with open("history.jsonl","r") as file:
     for line in file:
        line = line.strip()
        if line == "":
            continue                                    #also use json .dumps to make the append list into the string 
        message=json.loads(line)
        content += f"{message['role']} : {message['content']} \n"
        if message["role"]=="Assistant":
            content+="\n"
    return content

      
count=1      
def Api_key(input_data):

    global count
    history=previous_content()
    try:
        
        api_key=os.getenv("GEMINI_API_KEY")
        client=genai.Client(api_key=api_key)
        data=history +"\n\n"+input_data
        response=client.models.generate_content(
            model="gemini-3.6-flash", # correct it run the program
            contents=data,
            config={
                "system_instruction":""
                You are a customer support assistant.
                Be polite and professional.
                Answer questions about products.
                Help with orders.
                Handle complaints.
                Never invent an order status.
                Ask for required information when something is missing.
                Use the provided order data and previous conversation when relevant""
            }
            )
        # print("output :\n",response.txt) 
        return response.text
    except Exception as error:
         if count<4:
            print(f"Attempt {count} failed")  
            count +=1
            print("Retrying...") 
            time.sleep(3) 
            return Api_key(input_data)
         else:
             print("Error :API Request failed")
             return False
def display(): 
    global count
    print("-"*50)
    print("Program Started")
    time.sleep(3)
    print("-"*50)
    print("User logged in ")
    if previous_content() is not None:
        print("File Loaded Sucessfully")
    print("-"*50)
    print("Checking API Request :")
    time.sleep(3)

    if Api_key("a") is False:
        return
    else:
        print("API Connection Build Sucessfully")
    print("-"*50)
    data="Give your Introduction "
    while data.strip().lower()!="exit":
        result=Api_key(data)
        if (result!=None):
         print(result)
        if os.path.exists("history.jsonl"):
         with open("history.jsonl","a") as file:
          json.dump({
            "role":"user",
            "content":data
            },file)
          file.write("\n")
          json.dump({
            "role":"Assistant",
            "content":result
             },file)
          file.write("\n")

        print("-"*50)
        data=input("ENTER THE TEXT : ")
        count=1
    print("-"*50)
    print("\nThanks for your conversation\n")
    print("Python Program Stopped\n")
display()

"""

# 15 
import json
import os
import time
from google import genai
from dotenv import load_dotenv
load_dotenv()
import logging
count=1     
Model_Name="gemini-3.6-flash" 
History_lines=0
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"

)

def previous_content():
    try:
        content=""
        with open("history.jsonl","r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue                                    #also use json .dumps to make the append list into the string
                message=json.loads(line)
                content += f"{message['role']} : {message['content']} \n"                    
                if message["role"]=="Assistant":
                     content+="\n"
        return content
    except Exception as Error:
        logging.error(f"Previous content loading failed: {Error}")
        return None

def Api_key(input_data,System_instructions):

    global count
    history=previous_content()
    try:
        
        api_key=os.getenv("GEMINI_API_KEY")
        client=genai.Client(api_key=api_key)
        data=history +"\n\n"+input_data
        response=client.models.generate_content(
            model=Model_Name,
            contents=data,
            config={
                "system_instruction":System_instructions
            }
            )
        # print("output :\n",response.txt)
        return response.text
    except Exception as error:
         if count<4:
            print(f"Attempt {count} failed")
            logging.error(f"Error :API Request failed  Attempt {count} : {error}")
            count +=1
            print("Retrying...")
            time.sleep(3)
            return Api_key(input_data, System_instructions)
         else:
             print("Error :API Request failed")
             return False

def Switch_case():
    x=0
    while True:
        print("-"*50)
        print("1. Answer questions")
        print("2. Explain code")
        print("3. Generate code")
        print("4. Summarize text")
        print("5. History")
        print("6. Clear Current History")
        print("7. Model Selection")
        print("8. EXIT")
        print("-"*50)
        x=int(input("Enter Your Choice : "))
        match x:
            case 1:
                prompt_function("User Ask Question You have to answer it in sufficient content")
            case 2:
                code_prompt_function("Explain the code in detail not overexplained")
            case 3:
                prompt_function("Generate a code ")
            case 4:    
                prompt_function("Summarize the text in 4-5 Lines ")            
            case 5:    
                history_display_function()            
            case 6:    
                Clear_Current_history()            
            case 7:
                global Model_Name
                print("-"*50)    
                print(f"Current Model : {Model_Name}")
                Model_Name=input("Enter the Model Name :")
                print("Model Upgrated Sucessfully ")
                print("-"*50)
            case 8:
                logging.info("User logged out")
                print("\nThanks for your conversation\n")
                logging.info("Python Program Stopped")
                print("Python Program Stopped\n")
                break
            case _:
                print("Invalid input")
    return

def Program_check_function():
    print("-"*50)
    logging.info("Program Started")
    print("Program Started")
    time.sleep(3)
    print("-"*50)
    logging.info("User logged in ")
    print("User logged in ")
    if previous_content() is not None:
        logging.info("File Loaded Sucessfully")
        print("File Loaded Sucessfully")
    else:
        print("-"*50)
        print("Python Program Stopped\n")
        logging.info("Python Program Stopped")
        print("File Error / Unable to find the file")
        return False
    print("-"*50)
    print("Checking API Request :")
    time.sleep(3)

    if Api_key("a","Reply only with OK") is False:
        logging.error("Api Key failed")
        return False
    else:
        logging.info("API Connection Build Sucessfully")
        print("API Connection Build Sucessfully")
    return True

def Clear_Current_history():
    global History_lines
    if History_lines==0:
        print("No Current history in file to delete")
    else:
    
        with open("history.jsonl","r") as file:
            lines=file.readlines()
            if len(lines)<= History_lines:
                lines=[]
            else:
                lines=lines[:-History_lines]
        with open("history.jsonl","w") as file:
            file.writelines(lines)
                    
        print("Current History deleted Sucessfully")
        History_lines=0
    return

def prompt_function(System_instructions):
    global count
    input_data=""
    result=""
    while True:
        print("-"*50)
        input_data=input("ENTER THE TEXT : ")
        if input_data.strip().lower() in ["end", "exit"]:
            return
        else:
            result=Api_key(input_data,System_instructions)
        if result is not None and result is not False:
         print(result)
         conversation_save_function(result,input_data)
        count=1

def code_prompt_function(System_instructions):
    global count
    code_line_list=[]
    print("-"*50)
    print("Enter the code here :\n\n")
    while True:
        line=input()
        if line.strip().lower() in ["end", "exit"]:
            break
        code_line_list.append(line)
    content="\n".join(code_line_list)
    print("-----------------Code--exit---------------------")
    result=Api_key(content,System_instructions)
    if result is not None and result is not False:
        conversation_save_function(result,content)
        print(result)
    return

def history_display_function():
    print("-"*50)
    if os.path.exists("history.jsonl"):
         with open("history.jsonl","r") as file:
            for line in file:
                line=line.strip()
                if line=="":
                    continue
                message=json.loads(line)
                if message['role']=="user":
                    print("\n")
                print(f"{message['role']}  :  {message['content']}")
    return

def conversation_save_function(result,data):
    global History_lines
    History_lines+=2
    if os.path.exists("history.jsonl"):
         with open("history.jsonl","a") as file:
             if result is not None and result is not False:
                json.dump({
                    "role":"user",
                    "content":data
                    },file)
                file.write("\n")
                json.dump({
                    "role":"Assistant",
                    "content":result
                    },file)
                file.write("\n")

if Program_check_function():
    Switch_case()