
"""

#1 
data = [
    "I love NLP",
    "NLP is amazing",
    "I love coding"
]
Vocabulary=set()
List_of_vectors=[]
for line in data:
    tokens=line.split()
    Vocabulary.update(tokens)
Vocabulary=list(Vocabulary)
print("Vocabulary",Vocabulary)
for line in data:
    tokens=line.split()
    vector=[]
    for word in Vocabulary:
        vector.append(tokens.count(word))
    print(vector)
    List_of_vectors.append(vector)
for i in range(len(data)):
    print("Vector for line ",i+1," is ",List_of_vectors[i])
 
 #2
 
from sklearn.feature_extraction.text import CountVectorizer
corpus={
   "I love NLP and Machine Learning",
    "Machine Learning is amazing",
    "I love learning new things" 
}
vectorizer=CountVectorizer()
bow_matrix=vectorizer.fit_transform(corpus)
print("Vocabulary",vectorizer.get_feature_names_out())
print("\nBoW Sparse Matrix:\n",bow_matrix)
print("Bow Matrix \n",bow_matrix.toarray())


#3

from sklearn.feature_extraction.text import TfidfVectorizer
corpus={
    "I love NLP and Machine Learning",
    "Machine Learning is amazing",
    "I love learning new things"
}
vectorizer=TfidfVectorizer()
matrix=vectorizer.fit_transform(corpus)
print("Vocabulary",vectorizer.get_feature_names_out())
print("TF-IDF Matrix \n",matrix.toarray())


#4
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
text1 = "I love NLP"
text2 = "I enjoy NLP and text processing"
vectorizer=TfidfVectorizer()
Tfidf_matrix=vectorizer.fit_transform([text1,text2])
print("Vocabulary",vectorizer.get_feature_names_out())
print("TF-IDF Matrix \n",Tfidf_matrix.toarray())
print("Cosine Similarity \n",cosine_similarity(Tfidf_matrix))
print("Similarity  Score \n",cosine_similarity(Tfidf_matrix)[0][1])


#5 
from sklearn.feature_extraction.text import TfidfVectorizer
# from torch import cosine_similarity
from sklearn.metrics.pairwise import cosine_similarity
Resume="Python, Machine Learning, SQL, Deep Learning, NLP"
Job_Description="Looking for a Python developer with Machine Learning, NLP, SQL and Deep Learning skills"
vectorizer=TfidfVectorizer()
Tfidf_matrix=vectorizer.fit_transform([Resume,Job_Description])
print("Vocabulary",vectorizer.get_feature_names_out())
print("Cosine Similarity \n",cosine_similarity(Tfidf_matrix))
print("Matching percentage is  \n",cosine_similarity(Tfidf_matrix)[0][1]*100,"%")

# 6
import pandas as pd
import re
data=pd.read_csv("Spam.csv")
print(data.head())
print(data.shape) # finding the shape of the data
print("Columns name are :")
print(data.columns.tolist())
print(data["label"].value_counts())
print(data.head(5))

# 7
import re
import pandas as pd
def data_clean(text):
    text=str(text).lower()
    text=re.sub(r"\s+@\s+","",text)
    text=re.sub(r"[^a-z0-9\s]","",text)
    text=re.sub(r"\d+","",text)
    text=re.sub(r"\s+"," ",text)
    return(text)
data=pd.read_csv("resume.csv")
data["NEW DATA"] = data["Resume"].apply(data_clean)
data.to_csv("resume.csv",index=False)
print(data["Resume"])
print(data["NEW DATA"])

# 8

import pandas as pd
import re
data=pd.read_csv("resume.csv")
def data_clean(text):
    text=str(text).lower()
    text=re.sub(r"\s+@\s+","",text)
    text=re.sub(r"[^a-z0-9\s]","",text)
    text=re.sub(r"\d+","",text)
    text=re.sub(r"\s+"," ",text)
    return(text)
data["NEW DATA"] = data["Resume"].apply(data_clean)
def TOKENS(text):
    return(str(text).split())
data["tokens"]=data["Resume"].apply(TOKENS)
data.to_csv("resume.csv",index=False)
print("total number of tokens in row 1 = ",len(data["tokens"][0]))
print("20 tokens = ",data["tokens"].iloc[0][:20])

# 9
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
import pandas as pd
import re
def remove_stopwords(tokens):
  return [words for words in tokens if words not in stop_words]
data=pd.read_csv("resume.csv")
def data_clean(text):
    text=str(text).lower()
    text=re.sub(r"\s+@\s+","",text)
    text=re.sub(r"[^a-z0-9\s]","",text)
    text=re.sub(r"\d+","",text)
    text=re.sub(r"\s+"," ",text)
    return(text)
data["NEW DATA"] = data["Resume"].apply(data_clean)
def TOKENS(text):
    return(str(text).split())
data["tokens"]=data["Resume"].apply(TOKENS)
data["After Stop Words"]=data["tokens"].apply(remove_stopwords)
data.to_csv("resume.csv",index=False)
"""
# 10
import re
from nltk.corpus import stopwords
stop_word=set(stopwords.words("english"))
def Stop_word_removal(tokens):
    return [word for word in tokens if word not in stop_word]
file=open("NLP_Practice_Notes.txt",'r',encoding="utf-8")
data=file.read()
print("Original Data :")
print(data)
def clean_text(data):
    text=str(data).lower()
    text=re.sub(r"\s+@\s+","",text)
    text=re.sub(r"\d+","",text)
    text=re.sub(r"\s+"," ",text)
    text=re.sub(r"[^a-z\s]","",text)
    return text
New_text=clean_text(data)
print(New_text)
tokens=(New_text).split()
print("After tokenization")
print(tokens)
print(len(tokens))
clean_text=Stop_word_removal(tokens)
print("After Stop Word Removal")
print(clean_text)
print(len(clean_text))
