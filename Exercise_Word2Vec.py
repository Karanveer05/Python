"""
#1
from gensim.models import Word2Vec
sentences = [
    ["i", "went", "to", "the", "bank", "to", "withdraw", "money"],
    ["i", "sat", "by", "the", "river", "bank"],
    ["i", "drive", "my", "car", "to", "work"],
    ["i", "drive", "my", "automobile", "to", "work"],
]
model_cbow=Word2Vec(
    sentences,
    vector_size=5,
    window=3,
    min_count=1,
    sg=0
)
print("3 Vectors are :")
print(model_cbow.wv["went","i","drive"])
print(model_cbow.wv.vector_size)

#2

import pandas as pd
from gensim.models import Word2Vec
import pandas as pd
import ast
data = pd.read_csv("WordNet.csv")
print(data)
sentence = data["tokens"].apply(ast.literal_eval).tolist()
model_cbow=Word2Vec(
    sentence,
    vector_size=5,
    window=3,
    min_count=1,
    sg=0
)
print("3 Vectors are :")
print(model_cbow.wv["went","i","drive"])
print(model_cbow.wv.vector_size)
print(model_cbow.wv.most_similar(["money"],topn=1))

model_skip_gram=Word2Vec(
    sentence,
    vector_size=5,
    window=3,
    min_count=1,
    sg=1
)
print("-"*35)
print(model_skip_gram.wv["went","i","drive"])
print(model_skip_gram.wv.vector_size)
print(model_skip_gram.wv.most_similar(["money"],topn=1))

#3

from gensim.models import Word2Vec
import pandas as pd
import ast
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
data=pd.read_csv("wordNet.csv")
data["tokens"]=data["tokens"].apply(ast.literal_eval)
def remove_stopwords(text):
    return [word for word in text if word not in stop_words]
data["tokens"]=data["tokens"].apply(remove_stopwords)
data.to_csv("WordNet.csv")
sentences=data["tokens"].tolist()
# sentences=data["sentence"].str.split().tolist()
model_cbow=Word2Vec(
    sentences,
    vector_size=5,
    window=3,
    min_count=1,
    sg=0
)
print("3 Vectors are :")
print(model_cbow.wv.most_similar(["car"],topn=5))
print(model_cbow.wv.most_similar(["travel"],topn=5))
print(model_cbow.wv.most_similar(["drive"],topn=5))
print(model_cbow.wv.similarity("travel", "drive"))

#4
from gensim.models import Word2Vec
import pandas as pd
import ast
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
def Lemmatizer_words(text):
    return [lemmatizer.lemmatize(word) for word in text]
stop_words=set(stopwords.words("english"))
data=pd.read_csv("wordNet.csv")
data["tokens"]=data["tokens"].apply(ast.literal_eval)
def remove_stopwords(text):
    return [word for word in text if word not in stop_words]
data["tokens"]=data["tokens"].apply(remove_stopwords)
data["tokens"]=data["tokens"].apply(Lemmatizer_words)
data.to_csv("WordNet.csv",index=False)
sentences=data["tokens"].tolist()
# sentences=data["sentence"].str.split().tolist()     if the csv file contain the sentences
model_cbow=Word2Vec(
    sentences,
    vector_size=5,
    window=3,
    min_count=1,
    sg=0        #sg=1 if skip_ngram model
)
print("3 Vectors are :")
print(model_cbow.wv.most_similar(["car"],topn=5))
print(model_cbow.wv.most_similar(["travel"],topn=5))
print(model_cbow.wv.most_similar(["drive"],topn=5))
print(model_cbow.wv.similarity("car", "automobile"))
print(model_cbow.wv.similarity("drive", "work"))
print(model_cbow.wv.similarity("car", "river"))

## all the similarities depend upon the size of the data set and the cleaning of the dataset in this the data set size is not so big the match the similarity of words to the real word level similarity as it requires huge data set 

"""

#5
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model=SentenceTransformer(
    "all-MiniLM-L6-v2"
)
Resume="Python, Machine Learning, NLP, Pandas, NumPy, SQL"
person_1="Python, Machine Learning, NLP, Pandas, NumPy, SQL"

person_2="Java, Spring Boot, MySQL, HTML, CSS, JavaScript"

person_3="Python, Data Science, Deep Learning, NLP, SQL, Database Management"


Resume_embending=model.encode([Resume])
person_1_embending=model.encode([person_1])
person_2_embending=model.encode([person_2])
person_3_embending=model.encode([person_3])
similarity=cosine_similarity(Resume_embending,person_1_embending)[0][0]
print("person 1 matching creteria",similarity)
similarity=cosine_similarity(Resume_embending,person_2_embending)[0][0]
print("person 2 matching creteria",similarity)
similarity=cosine_similarity(Resume_embending,person_3_embending)[0][0]
print("person 3 matching creteria",similarity)