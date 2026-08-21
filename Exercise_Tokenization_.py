#1
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize,word_tokenize
paragraph=str(input("enter the paragraph : "))
list_of_sentence_tokens=sent_tokenize(paragraph)
print(list_of_sentence_tokens)
print(f"total no of sentence tokens are : {len(list_of_sentence_tokens)}")
for i,sentence in enumerate(list_of_sentence_tokens,start=1):
    print(f"\nSentence {i}")
    list_of_words_tokens=word_tokenize(sentence)
    word_only=[
        word for word in list_of_words_tokens
        if word.isalpha()
    ]
    print(word_only)
    print(f"total no of words : {len(word_only)}")
#2
import nltk
import pandas as pd
from nltk.tokenize import sent_tokenize,word_tokenize
Example="Python is powerful and Python is easy. Python is popular."
Example=Example.lower()
print(Example)
word_tokens=word_tokenize(Example)
Word_only=[
    word for word in word_tokens
    if word.isalpha()
]
print(Word_only)
Word_only=pd.Series(Word_only)
frequency=Word_only.value_counts()
print(frequency)
max_count=frequency.max()
print(f"most frequently occur tokens are :\n{frequency[frequency==max_count]}")
#3
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
    if word.isalpha()
]
print(f"Alphabetic Character : {Alphabetic}")
Numeric=[
    word for word in Word_tokens
    if int_float(word)
]
print(f"Numeric Character : {Numeric}")
Special=[
    word for word in Word_tokens
    if not (word.isalpha() or int_float(word))
]
print(f"Special Characters : {Special}")
#4
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
print(f"Unique tokens are :\n{unique_tokens.unique()}")
print(f"Number of Unique tokens : {len(unique_tokens.unique())}")
Alphabetic=[
    word for word in Word_tokens
    if word.isalpha()
]
Numeric=[
    word for word in Word_tokens
    if int_float(word)
]
Special=[
    word for word in Word_tokens
    if not (word.isalpha() or int_float(word))
]
print(f"number of alphabetic tokens is : {len(Alphabetic)}")
print(Alphabetic)
print(f"number of Numeric tokens is : {len(Numeric)}")
print(Numeric)
print(f"number of Special tokens is : {len(Special)}")
print(Special)
longest_token=max(Word_tokens,key=len)
shortest_token=min(Word_tokens,key=len)
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
#6
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
print(f"After Sentence Tokenization : {sentence_tokens}")
word_token=[]
for sentence in sentence_tokens:
    word_token.extend(word_tokenize(sentence))
print(f"After Word Tokenization : {word_token}")
lowercase_tokens=[
    word.lower() for word in word_token
]
print(f"After Lowercasing : {lowercase_tokens}")
punctuation_removed=[
    word for word in lowercase_tokens
    if word.isalpha() or numerical_value_check(word)
]
print(f"After Punctuation Removal : {punctuation_removed}")
stopword_removed=[
    word for word in punctuation_removed
    if word not in stop_words
]
print(f"After Stopword Removal : {stopword_removed}")
final_tokens_list=[
    word for word in stopword_removed
    if word.isalpha() or numerical_value_check(word)
]
print(f"Final Tokens : {final_tokens_list}")
#7
import nltk
from nltk.tokenize import word_tokenize,RegexpTokenizer
text="Hello, world! NLP is amazing. Python's power is incredible."
using_split=text.split()
print(f"Using split() : {using_split}")
word_tokenizer=word_tokenize(text)
print(f"Using word_tokenize() : {word_tokenizer}")
tokens=RegexpTokenizer(r"\w+")
Reg_exp_tokens=tokens.tokenize(text)
print(f"Using RegexpTokenizer : {Reg_exp_tokens}")
print("Difference :")
print("split() keeps punctuation attached with the words.")
print("word_tokenize() separates punctuation as different tokens.")
print("RegexpTokenizer removes punctuation and returns only word characters.")
print("word_tokenize() handles punctuation better when punctuation is required as separate tokens.")
print("RegexpTokenizer handles punctuation better when punctuation has to be removed.")
#8
import re
Input="I love #Python and #AI! Check https://example.com @student123 :blush: 123 😊"
Hastags=re.findall(r"#\w+",Input)
print(f"Hashtags : {Hastags}")
Mentions=re.findall(r"@\w+",Input)
print(f"Mentions : {Mentions}")
Url_s=re.findall(r"https?://\S+",Input)
print(f"URLs : {Url_s}")
Numbers=re.findall(r"\b\d+(?:\.\d+)?\b",Input)
print(f"Numbers : {Numbers}")
Normal_words=re.findall(r"\b[A-Za-z]+\b",re.sub(r"#\w+|@\w+|https?://\S+|:\w+:","",Input))
print(f"Normal Words : {Normal_words}")
Special=[
    character for character in Input
    if not character.isalnum() and not character.isspace()
]
print(f"Special Characters/Emojis : {Special}")
clean_text=re.sub(r"#\w+|@\w+|https?://\S+|:\w+:","",Input)
print(f"Normal text : {clean_text}")
#9
import pandas as pd
from nltk.tokenize import word_tokenize
Input=pd.Series(["playing","unhappiness","internationalization","misunderstanding","machinelearning"])
def Character_tokenizer(word):
    character_token=[]
    for character in word:
        character_token.extend(character)
    return character_token
Character_level=Input.apply(Character_tokenizer)
print(f"Character Level Tokenization :\n{Character_level}")
def Word_tokenizer(word):
    return word_tokenize(word)
Word_level=Input.apply(Word_tokenizer)
print(f"Word Level Tokenization :\n{Word_level}")
def Subword_tokenizer(word):
    subword_token=[]
    for i in range(0,len(word),3):
        subword_token.append(word[i:i+3])
    return subword_token
Subword_level=Input.apply(Subword_tokenizer)
print(f"Subword Style Tokenization :\n{Subword_level}")
print("Conclusion :")
print("Character-level tokenization splits every word into individual characters.")
print("Word-level tokenization keeps each complete word as a token.")
print("Subword-style tokenization divides words into smaller parts.")
#10
import nltk
import re
import pandas as pd
from nltk.corpus import stopwords
Stop_words=set(stopwords.words("english"))
from nltk.tokenize import word_tokenize,sent_tokenize
paragraph=str(input("Enter the paragraphs : "))
sentence_tokens=sent_tokenize(paragraph)
print(f"Number of Sentences : {len(sentence_tokens)}")
print(f"Sentence Tokens : {sentence_tokens}")
Word_tokens=[]
for sentence in sentence_tokens:
    Word_tokens.extend(word_tokenize(sentence))
def int_float(token):
    token=re.sub(r"\.",'',token)
    if token.isdigit():
        return True
    else:
        return False
print(f"Number of tokens : {len(Word_tokens)}")
print(f"Word Tokens : {Word_tokens}")
unique_tokens=pd.Series(Word_tokens)
print(f"Unique tokens are :\n{unique_tokens.unique()}")
print(f"Number of Unique tokens : {len(unique_tokens.unique())}")
common_tokens=pd.Series(Word_tokens)
print(f"Top 5 Most Common tokens are :\n{common_tokens.value_counts().head(5)}")
Alphabetic=[
    word for word in Word_tokens
    if word.isalpha()
]
Numeric=[
    word for word in Word_tokens
    if int_float(word)
]
Special=[
    word for word in Word_tokens
    if not (word.isalpha() or int_float(word))
]
print(f"number of alphabetic tokens is : {len(Alphabetic)}")
print(Alphabetic)
print(f"number of Numeric tokens is : {len(Numeric)}")
print(Numeric)
print(f"number of Special tokens is : {len(Special)}")
print(Special)
stop_words_number=[
    word for word in Word_tokens
    if word.lower() in Stop_words
]
clean_text=[
    word for word in Word_tokens
    if word.lower() not in Stop_words and (word.isalpha() or int_float(word))
]
longest_token=max(Word_tokens,key=len)
shortest_token=min(Word_tokens,key=len)
print(f"Longest token is : {longest_token}")
print(f"Shortest token is : {shortest_token}")
print(f"Number of Stop Words is : {len(stop_words_number)}")
print(f"clean text is : {clean_text}")
total_length=0
for word in Word_tokens:
    total_length=total_length+len(word)
average_length=total_length/len(Word_tokens)
print(f"Average token length is : {average_length}")