import pandas as pd
from sentence_transformers import SentenceTransformer
import re
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st
# st.title("🎬 Movie Recommendation System")
# Stop_words=set(stopwords.words("english"))
# lemmantizer=WordNetLemmatizer()
data=pd.read_csv("movie_recommendation_uncleaned.csv")
# print(data)
# data["Rating"]=data["Rating"].fillna(data["Rating"].mean())
# # data["Movie_Name"]=data["Movie_Name"].dropna()
# data=data.dropna(subset=["Movie_Name"])
# data=data.dropna(subset=["Genre"])
# data=data.dropna(subset=["Description"])
# data=data.dropna(subset=["Release_Year"])
# data=data.drop_duplicates()
# data["Rating"]=data["Rating"].abs()
# data["Release_Year"]=data["Release_Year"].abs()
# data.to_csv("movie_recommendation_uncleaned.csv",index=False)
# print(data.isnull().sum())
# print((data["Rating"]<0).sum())
# print((data["Release_Year"]<0).sum())
# print(data.duplicated().sum())
# def data_clean_tokens(text):
#     text=str(text).lower()
#     text=re.sub("\s+@\s+","",text)
#     text=re.sub("\d+","",text)
#     text=re.sub("\s+"," ",text)
#     text=re.sub("[^a-z\s]","",text)
#     token=text.split()
#     return(token)
# def Stop_Words(token):
#     return[word for word in token if word not in Stop_words]
# def lemmatize(token):
#     return[lemmantizer.lemmatize(words) for words in token]
# data["Tokenised"]=data["Description"].apply(data_clean_tokens)
# data["Tokenised"]=data["Tokenised"].apply(Stop_Words)
# data["Tokenised"]=data["Tokenised"].apply(lemmatize)
# data["Movie_Name"] = data["Movie_Name"].astype(str).str.lower()
# data["Tokenised"]=data["Tokenised"].apply(lambda words: "_".join(words))
# data["Genre"]=data["Genre"].astype(str).str.lower()
# data.to_csv("movie_recommendation_uncleaned.csv",index=False)
Movie_name_input=str(input("Enter the movie Name : ")).lower()
# Movie_name_input=st.text_input("Enter the Movie Name ").lower()
        
model=SentenceTransformer(
    "all-MiniLM-L6-V2"
)
# if st.button("Recommend"):
#  if Movie_name_input=="":
#          st.warning("Enter the Movie Name")
#  else:
User_Movie_name_emmbedings=model.encode([Movie_name_input])
movies_in_dataset_emmbedings=model.encode(data["Movie_Name"].astype(str).tolist())
similarity=cosine_similarity(User_Movie_name_emmbedings,movies_in_dataset_emmbedings)[0]
Index_of_Matching_movie=similarity.argmax()
Movie_Name=data.iloc[Index_of_Matching_movie]["Movie_Name"]                 
Movie_ID=data.iloc[Index_of_Matching_movie]["Movie_ID"]
Movie_Genre=data.iloc[Index_of_Matching_movie]["Genre"]
# st.write(f"Movie Name Is {Movie_Name}")
print(Movie_Name)
Genre_based_movie=data[data["Genre"]==Movie_Genre]
Genre_based_movie.to_csv(f"{Movie_Genre}.csv", index=False)
New_data=pd.read_csv(f"{Movie_Genre}.csv")
Movie_description=New_data[New_data["Movie_ID"]==Movie_ID]
# print(Movie_description["Tokenised"])

Movie_Description_emmbedings=model.encode(Movie_description["Tokenised"].astype(str).tolist())
Movies_in_dataset_emmbedings=model.encode(New_data["Tokenised"].astype(str).tolist())
similarity=cosine_similarity(Movie_Description_emmbedings,Movies_in_dataset_emmbedings)
similarity = cosine_similarity(
    Movie_Description_emmbedings,
    Movies_in_dataset_emmbedings
)[0]

New_data.iloc[similarity]["Movie_Name"]
sorted_index=similarity.argsort()[::-1]
# for index in sorted_index[1:6]:
#     print(New_data.iloc[index]["Movie_Name"])
st.subheader("Recommended Movies")
for index in sorted_index[1:6]:
    st.write(New_data.iloc[index]["Movie_Name"])