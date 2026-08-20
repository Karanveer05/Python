
"""
from datasets import load_dataset
from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
import numpy as np
import torch
import evaluate
accuracy=evaluate.load("accuracy")
#Load the dataset
dataset=load_dataset("sh0416/ag_news")
# print(dataset)

# fetch smaller dataset from the Load datasets  1.15  
train_dataset=(
    dataset["train"]
    .shuffle(seed=42)
    .select(range(2000))
)
test_dataset=(
    dataset["test"]
    .shuffle(seed=42)
    .select(range(500))
)

print("\nTraining Samples : ",len(train_dataset))

# checking samples

# print("\nTraining Samples : ",train_dataset[0])
# print("\nTraining Samples : ",train_dataset[1])

#model selection

model_name="distilbert-base-uncased"
tokenizer=AutoTokenizer.from_pretrained(model_name)

def tokenize_function(input_data):
    return tokenizer(
        input_data["description"],
        truncation=True,
        padding="max_length",
        max_length=128
    )
    
    # distilbert loaded

tokenize_train=train_dataset.map(tokenize_function,batched=True)
tokenize_test=test_dataset.map(tokenize_function,batched=True)
model=AutoModelForSequenceClassification.from_pretrained(model_name,num_labels=4)

#
def compute_metrics(eval_pred):
    predictions,labels=eval_pred
    predictons=np.argmax(
        predictions,
        axis=1
    )
    return accuracy.compute(
        predictions=predictions,
        references=labels
    )
training_args=TrainingArguments(
    output_dir="./agnews_model",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenize_train,
    eval_dataset=tokenize_test,
    compute_metrics=compute_metrics
)
trainer.train()
result=trainer.evaluate()
print(result)

save_path="./agnews_model"
trainer.save_model(save_path)
tokenizer.save_pretrained(save_path)
print(save_path)

texts = [

    "I absolutely loved this movie!",

    "This movie was boring and terrible.",

    "The acting was excellent and the story was fantastic.",

    "I did not enjoy this movie at all."

]

def predict_news(text):
    
    inputs=tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True
 )
    inputs={
    key:value.to(model.device)
    for key,value in inputs.items()
 }
    with torch.no_grad():
     outputs=model(**inputs)

    prediction=torch.argmax(
     outputs.logits,
     dim=1
    ).item()

    if prediction ==1:
     return "positive"
    else:
     return "Negitive"

#1

#Installing Required Libraries
from datasets import load_dataset
from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
import torch
import evaluate

#Fetch the data set online from huggingface model
dataset=load_dataset("sh0416/ag_news")
# print(dataset)
print(set(dataset["train"]["label"]))

#create the smaller data set from huge dataset we fetched above
train_dataset=(
    dataset["train"]
    .shuffle(seed=42)
    .select(range(2000))
)

test_dataset=(
    dataset["test"]
    .shuffle(seed=42)
    .select(range(2000))
)
print(train_dataset.column_names)
print(len(train_dataset))
print(train_dataset.features)      #like -- dtypes
print(train_dataset[:5])



#2
import torch
from datasets import load_dataset
import evaluate
from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)

dataset=load_dataset("sh0416/ag_news")
# print(set(dataset["train"]["label"]))
# print(dataset[:5])
# print(dataset.column_names)
# print(len(dataset))
# print(dataset["train"].features)

train_dataset=(
    dataset["train"]
    .shuffle(seed=1)
    .select(range(200))
)
test_dataset=(
    dataset["test"]
    .shuffle(seed=1)
    .select(range(20))
)

#load the model
model_used="distilbert-base-uncased"

#Load tokenizer acc to pretrained model              Exercise_transformer_huggingface.py
tokenizer=AutoTokenizer.from_pretrained(model_used)

def tokenizer_function(data):
    return tokenizer(
     data["description"],
     truncation=True,
     padding="max_length",
     max_length=64
     )
    
tokenized_train=train_dataset.map(tokenizer_function,batched=True)
print(tokenized_train["title"][0])
print(tokenized_train["description"][0])
print(tokenized_train["input_ids"][0])
print("Conversion")
print(tokenizer.convert_ids_to_tokens(
    tokenized_train[0]["input_ids"]
))

#3
from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from datasets import load_dataset
import torch
import evaluate
import numpy as np
print("Step 1 pass")
dataset=load_dataset("sh0416/ag_news")
print("Step 2 pass")
# print(dataset)
# print(set(dataset["train"]["label"]))
# print(dataset[:5])
# print(dataset["train"].features)
train_dataset=(
    dataset["train"]
    .shuffle(seed=42)
    .select(range(200))
)
train_dataset=(
    dataset["train"]
    .shuffle(seed=42)
    .select(range(200))
)

print("Step 3 pass")
print(train_dataset[:5])
print(train_dataset.column_names)
print(train_dataset.features)
print(len(train_dataset))

print("Step 3 pass")
model_name="distilbert-base-uncasted"
tokenizer=AutoTokenizer.frompretrained(model_name)
def tokenizer_function(data):
    return tokenizer(
        data["description"],
        truncation=True,
        padding="max_length",
        max_length=64
    )
    # tokem_set contain all the tokens ids and title and description of articles 
print("Step 4 pass")
tokens_set_of_train_dataset=train_dataset.map(tokenizer_function,batched=True)
tokens_set_of_test_dataset=train_dataset.map(tokenizer_function,batched=True)
# print(tokens_set_of_train_dataset["title"][0])
# print(tokens_set_of_train_dataset["description"][0])
# print(tokens_set_of_train_dataset["input_ids"][0])
# print(tokenizer.convert_ids_to_tokens(tokens_set_of_train_dataset[0]["input_ids"]))

model=AutoModelForSequenceClassification.from_pretrained(model_name,num_labels=4)

print("Step 5 pass")
accuracy=evaluate.load("accuracy")

train_args=TrainingArguments(
    output="./ag_news_model",
    eval_strategy="epoch",
    num_train_epoch=2,
    learnig_rate=2e-5,
    per_device_eval_batch_size=16,
    per_device_train_batch_size=16,
    weight_decay=0.01,
    report_to="none"
)

def compute_metrics(eval_pred):
    predictions,labels=eval_pred
    predictions=np.argmax(predictions,axis=1)
    return accuracy.compute(predictions=predictions,references=labels)
    
trainer=Trainer(
    model=model,
    args=train_args,
    train_dataset=tokens_set_of_train_dataset,
    eval_dataset=tokens_set_of_test_dataset,
    compute_metrics=compute_metrics
)

print("Step 7 pass")
trainer.train()
print("Step 8 pass")
print('I love this movie')
result=trainer.evaluate()
print(result)


# 4 
from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from datasets import load_dataset
import numpy as np
import torch
import evaluate

dataset=load_dataset("sh0416/ag_news")
# print(dataset)
# print(set(dataset["train"]["label"]))
# print(dataset[:5])
# print(len(dataset))
train_dataset=(
    dataset["train"]
    .shuffle(seed=42)
    .select(range=200)
)
test_dataset=(
    dataset["test"]
    .shuffle(seed=42)
    .select(range=200)
)
# print(train_dataset[:5])
model_name="distilbert-base-uncased"
tokenizer=AutoTokenizer.from_pretrained(model_name)
def tokenizer_function(data):
    return tokenizer(
        data["text"],
        truncation=True,
        padding="max_length",
        max_length=64
    )
train_tokens_set=train_dataset.map(tokenizer_function,batched=True)
test_tokens_set=test_dataset.map(tokenizer_function,batchedd=True)
# print(train_tokens_set["input_ids"][0])
# print(tokenizer.convert_ids_to_tokens(train_tokens_set["input_ids"][0]))
model=AutoModelForSequenceClassification.from_pretrained(model_name,num_labels=4)
training_args=TrainingArguments(
    output_dir="/.ag_news",
    eval_strategy="epoch",
    num_train_epochs=2,
    learning_rate=2e-5,
    weight_decay=0.01,
    per_device_eval_batch_size=16,
    per_device_train_batch_size=16,
    report_to="none"
)
accuracy=evaluate.load("accuracy")
def compute_metrics(eval_pred):
    predictions,labels=eval_pred
    predictions=np.argmax(predictions,axis=1)
    return accuracy.compute(predictions=predictions,reference=labels)
trainer=Trainer(
    model=model,
    args=training_args,
    train_dataset=train_tokens_set,
    eval_dataset=test_tokens_set,
    compute_metrics=compute_metrics
)
trainer.train()
trainer.evaluate()

save_path="./ag_new_model"
trainer.save_model(save_path)
tokenizer.save_pretrained(save_path)

def predict_sentiment(text):
    inputs=tokenizer(
        text,
        return_tensors="pt",
        truncation="True",
        padding="True"
    )
    inputs={
        key:value.to(model.device)
        for key,value in inputs.items()   
    }
    with torch.no_grad():
        outputs=model(**inputs)
        prediction=torch.argmax(
            outputs.logits,
            dim=1
        ).item()
    if prediction==1:
        return "World"
    elif prediction==2:
        return "Sports"
    elif prediction==3:
        return "Business"
    elif prediction==4:
        return "Sci/tech"
        
    
texts = [

    "The government announced a new international agreement.",

    "The cricket team won the championship after a thrilling match.",

    "Stock markets increased after the company reported record profits.",

    "Scientists developed a new artificial intelligence technology."

]
for text in texts:

    result = predict_sentiment(text)

    print("Text:", text)
    print("Prediction:", result)
    
    """
    
# 5 
from transformers import(
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
import torch

save_path="./ag_new_model"

model_name=(save_path)
tokenizer=AutoTokenizer.from_pretrained(model_name)
model=AutoModelForSequenceClassification.from_pretrained(model_name)
def predict_sentiment(text):
    inputs=tokenizer(
        text,
        return_tensors="pt",
        truncation="True",
        padding="True",
        max_length=64
    )
    inputs={
        key:value.to(model.device)
        for key,value in inputs.items()   
    }
    with torch.no_grad():
        outputs=model(**inputs)
        prediction=torch.argmax(
            outputs.logits,
            dim=1
        ).item()
    if prediction==1:
        return "World"
    elif prediction==2:
        return "Sports"
    elif prediction==3:
        return "Business"
    elif prediction==4:
        return "Sci/tech"
        
    
texts = [

    "The government announced a new international agreement.",

    "The cricket team won the championship after a thrilling match.",

    "Stock markets increased after the company reported record profits.",

    "Scientists developed a new artificial intelligence technology."

]
for text in texts:

    result = predict_sentiment(text)

    print("Text:", text)
    print("Prediction:", result)