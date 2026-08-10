#1
"""
import pandas as pd
data=pd.read_csv("news_category.csv")
print(data.shape)
print(data.columns[::1])
print(data.head(5))
print(data.tail(5))
print(data.isnull().sum())
print(data.duplicated().sum())
data=data.drop_duplicates()
data=data.dropna()
data.to_csv("news_category.csv",index=False)
print(data["Category"].value_counts())


#2
import pandas as pd
import re
import nltk
# nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
data=pd.read_csv("news_category.csv")
stop_words=set(stopwords.words("english"))
lemmatizer=WordNetLemmatizer()
def clean_text(text):
    text=str(text).lower()
    text=re.sub(r"\s+@\s+","",text)
    text=re.sub(r"\d+","",text)
    text=re.sub(r"[^a-z\s+]","",text)
    text=re.sub(r"\s+"," ",text)
    return text
def make_tokens(text):
    return text.split()
def remove_stopwords(tokens):
    return[ word for word in tokens if word not in stop_words]
def lemmantize_tokens(tokens):
    return[lemmatizer.lemmatize(word) for word in tokens]
data["Cleaned_text"]=data["Description"].apply(clean_text)
data["tokens"]=data["Cleaned_text"].apply(make_tokens)
data["Stopwords_removed"]=data["tokens"].apply(remove_stopwords)
data["Lemmantize_tokens"]=data["Stopwords_removed"].apply(lemmantize_tokens)
data["final_text"] = data["Lemmantize_tokens"].apply(lambda words: " ".join(words))
data.to_csv("news_category.csv",index=False)


#3
import pandas as pd
data=pd.read_csv("news_category.csv")
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(

    # Keep maximum 3000 important features(words)
    max_features=3000,

    # Keep words appearing in at least 1 document
    min_df=1,

    # Keep words appearing in up to 100% documents
    max_df=1.9,

    # Use both Unigrams (1 word) and Bigrams (2 consecutive words)
    ngram_range=(1,2)
)
X=tfidf.fit_transform(data["final_text"])
print(X.shape)
print(tfidf.get_feature_names_out()[:20])

#4
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report            # Performance metrics
data=pd.read_csv("news_category.csv")

tfidf=TfidfVectorizer(
    max_features=3000,
    min_df=1,
    max_df=1.0,
    ngram_range=(1,2)
)
X=tfidf.fit_transform(data["final_text"])
y=data["Category"]    # prediction 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_predict=model.predict(X_test)
print(list(model.classes_))
print(list(y_predict[:10]))
print(list(y_test[:10]))
print(classification_report(y_test, y_predict))

"""

#5
import pandas as pd
import re
import matplotlib.pylab as plt
import seaborn as sns
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report,confusion_matrix
data=pd.read_csv("news_category.csv")
tfidf=TfidfVectorizer(
    max_features=3000,
    min_df=1,
    max_df=1,
    ngram_range=(1,2)
)
X=tfidf.fit_transform(data["final_text"])
y=data["Category"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_predict=model.predict(X_test)
stop_words=set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
data=pd.read_csv("news_category.csv")
def Clean_text(text):
    text=str(text).lower()
    text=re.sub(r"\s+@\s+","",text)
    text=re.sub(r"\s+"," ",text)
    text=re.sub(r"\d+","",text)
    text=re.sub(r"[^a-z\s+]","",text)
    return text
def Split_words(text):
    tokens=text.split()
    return tokens
def remove_Stop_Words(tokens):
    return[word for word in tokens if word not in stop_words]
def lemmantize_tokens(tokens):
    return[lemmatizer.lemmatize(word) for word in tokens]
data["Cleaned_text"]=data["Description"].apply(Clean_text)
data["tokens"]=data["Cleaned_text"].apply(Split_words)
data["Stopwords_removed"]=data["tokens"].apply(remove_Stop_Words)
data["Lemmantize_tokens"]=data["Stopwords_removed"].apply(lemmantize_tokens)
data["final_text"] = data["Lemmantize_tokens"].apply(lambda words: " ".join(words))
data.to_csv("news_category.csv",index=False)
print(list(model.classes_))
print(list(y_test[:10]))
print(list(y_predict[:10]))
print(classification_report(y_test,y_predict))
print(confusion_matrix(y_test,y_predict))
sns.heatmap(
    confusion_matrix(y_test,y_predict),
    annot=True,
    fmt="d",
    cmap="Blues",
    linewidths=0.5,
    linecolor="black",
    xticklabels=model.classes_,
    yticklabels=model.classes_
    
)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")

# Rotate category names
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

# Adjust layout
plt.tight_layout()

# Save image
plt.savefig("confusion_matrix.png")

print("\nConfusion matrix image saved as 'confusion_matrix.png'")

# Display plot
plt.show()