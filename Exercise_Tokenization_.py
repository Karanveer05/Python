"""

#1 

import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize,word_tokenize
paragraph=str(input("enter the paragraph : "))
list_of_sentence_tokens=sent_tokenize(paragraph)
print(list_of_sentence_tokens)
print(f"total no of tokens are : {len(list_of_sentence_tokens)} ")
for i ,sentence in enumerate(list_of_sentence_tokens,start=1):
    print(f"\nSentence {i}")
    print(f"total no of words : {len(sentence)}")
    list_of_words_tokens=word_tokenize(sentence)
    word_only=[
        word for word in list_of_words_tokens
        if word.isalpha()
    ]
    print(word_only)
    print(len(word_only))


# 2

import nltk
import pandas as pd
from nltk.tokenize import sent_tokenize,word_tokenize
Example="Python is powerful and Python is easy. Python is popular."
Example=Example.lower()
print(Example)
word_tokens=word_tokenize(Example)
Word_only=[
    word for word in word_tokens
        if word.isalpha()          # remove the dot 
]
print(Word_only)
Word_only=pd.Series(Word_only)
# frequency=Word_only.value_counts()
print(Word_only.value_counts())
print(f"most frequently occur tokens are :\n{Word_only.value_counts().head(2)}")
# for word,count in frequency.items():
#     print(f"{word}  :  {count}")


# 3
import nltk
import re
from nltk.tokenize import word_tokenize
Input="Python 3.12 is amazing! I have 2 projects"
Word_tokens=word_tokenize(Input)
def int_float(token):
    token=re.sub(r"\.",'',token)
    if token.isdigit():
       return True
    else:
        return False
Alphabetic=[
    word for word in Word_tokens
    if  word.isalpha() 
]
print(f"Alphabetic Character : {Alphabetic}")
Numeric=[
    word for word in Word_tokens
    if  int_float(word)
]
print(f"Numeric Character : {Numeric} ")
Special=[
    word for word in Word_tokens
     if  not (word.isalpha() or  int_float(word))
]
print(f"Special Characters : {Special}")


# 4
import nltk
import re
import pandas as pd
from nltk.tokenize import word_tokenize
paragraph=str(input("Enter the paragraphs : "))
Word_tokens=word_tokenize(paragraph)
def int_float(token):
    token=re.sub(r"\.",'',token)
    if token.isdigit():
       return True
    else:
        return False
print(f"Number of tokens : {len(Word_tokens)}")
unique_tokens=pd.Series(Word_tokens)
print(f"Unique tokens are :\n{unique_tokens.value_counts()[unique_tokens.value_counts()==1]}")
Alphabetic=[
    word for word in Word_tokens
    if  word.isalpha() 
]
Numeric=[
    word for word in Word_tokens
    if  int_float(word)
]
Special=[
    word for word in Word_tokens
     if  not (word.isalpha() or  int_float(word))
]
print(f"number of alphabetic tokens is : {len(Alphabetic)}")
print(Alphabetic)
print(f"number of Numeric tokens is : {len(Numeric)}")
print(Numeric)
print(f"number of Special tokens is : {len(Special)}")
print(Special)
longest_token = max(Word_tokens, key=len)
shortest_token = min(Word_tokens, key=len)
print(f"Longest token is : {longest_token}")
print(f"Shortest token is : {shortest_token}")



#5
import nltk
import re
from nltk.tokenize import word_tokenize
Input="Python 3.12 is amazing! I have 2 projects"
Word_tokens=word_tokenize(Input.lower())
def remove_tokens(token):
    if len(token)<3:
        return False
    else:
        return True
Word_tokens=[
     word for word in Word_tokens
     if word.isalpha() and remove_tokens(word)
]
print(Word_tokens)


# 6
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
stop_words=set(stopwords.words("english"))
def numerical_value_check(token):
    token=re.sub(r"\.",'',token)
    if token.isdigit():
       return True
    else:
        return False
Original_Text="Python is an amazing programming language! 1 2 3"
sentence_tokens=sent_tokenize(Original_Text)
final_tokens_list=[]
for sentence in sentence_tokens :
    word_token=word_tokenize(sentence.lower())
    word_filtering=[
        word for word in word_token
        if (word.isalpha() and word not in stop_words) or numerical_value_check(word)
    ]
    final_tokens_list.extend(word_filtering)
print(final_tokens_list)


# 7


import nltk
from nltk.tokenize import word_tokenize,RegexpTokenizer
text="Hello, world! NLP is amazing. Python's power is incredible."
using_split=text.split()
print(using_split)    # dont split the special characters as different tokens
word_tokenizer=word_tokenize(text)
print(word_tokenizer) # split the special characters as tokens
tokens=RegexpTokenizer(r"\w+")
Reg_exp_tokens=tokens.tokenize(text)
print(Reg_exp_tokens) # dont consider special characters as tokens




#8 

import re
Input="I love #Python and #AI! Check https://example.com @student123 :blush:"
Hastags=re.findall(r"#\w+",Input)
print(Hastags)
Mentions=re.findall(r"@\w+",Input)
print(Mentions)
Url_s=re.findall(r"https?\S+",Input)
print(Url_s)
clean_text=[re.sub(r"#\S+|@\w+|https?\S+|:\w+:","",Input)]
print(f"Normal text : {clean_text}")




#9

import pandas as pd 
Input=pd.Series(["playing", "unhappiness", "internationalization",
 "misunderstanding", "machinelearning"])
# def Character_tokenizer(word):
#     character_token=[]
#     for character in word:
#         character_token.extend(character)
#     return character_token
# print(Input.apply(Character_tokenizer))
 # doubt --- how word_tokenisation apply on list as they are already words  and how to target sub word tokenisation in the list 
"""
#10
import nltk
import re
import pandas as pd
from nltk.corpus import stopwords
Stop_words=set(stopwords.words("english"))
from nltk.tokenize import word_tokenize,sent_tokenize
paragraph=str(input("Enter the paragraphs : "))
sentence_tokens=sent_tokenize(paragraph)
print(f"Number of Sentences : {sentence_tokens}")
Word_tokens=[]
for sentence in sentence_tokens:
 Word_tokens.extend(word_tokenize(sentence_tokens))
def int_float(token):
    token=re.sub(r"\.",'',token)
    if token.isdigit():
       return True
    else:
        return False
print(f"Number of tokens : {len(Word_tokens)}")
common_tokens=pd.Series(Word_tokens)
max_count = common_tokens.value_counts().max()
print(f"Most Common tokens are :\n{common_tokens.value_counts()[common_tokens.value_counts()==max_count].head(5)}")
Alphabetic=[
    word for word in Word_tokens
    if  word.isalpha() 
]
Numeric=[
    word for word in Word_tokens
    if  int_float(word)
]
Special=[
    word for word in Word_tokens
     if  not (word.isalpha() or  int_float(word))
]
print(f"number of alphabetic tokens is : {len(Alphabetic)}")
print(Alphabetic)
print(f"number of Numeric tokens is : {len(Numeric)}")
print(Numeric)
print(f"number of Special tokens is : {len(Special)}")
print(Special)
stop_words_number=[
    word for word in Word_tokens
    if word in Stop_words
]
clean_text=[
    word for word in Word_tokens
    if word not in Stop_words and  (word.isalpha() or  int_float(word))
]
longest_token = max(Word_tokens, key=len)
shortest_token = min(Word_tokens, key=len)
print(f"Longest token is : {longest_token}")
print(f"Shortest token is : {shortest_token}")
print(f" Number of Stop Words is : {len(stop_words_number)}")
print(f" clean text is  is : {clean_text}")
# how to find average length of tokens ??
# under construction to remove error

