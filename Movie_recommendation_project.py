import pandas as pd
from sentence_transformers import SentenceTransformer
import re
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st
st.title("🎬 Movie Recommendation System")
data = pd.read_csv("movie_recommendation_uncleaned.csv")
Movie_name_input = st.text_input("Enter the Movie Name : ").lower().strip()
def load_model():
    return SentenceTransformer("all-MiniLM-L6-V2")
model = load_model()
# Recommend Button 
if st.button("Recommend"):
    if Movie_name_input == "":
        st.warning("Please enter a Movie Name.")
    else:
        with st.spinner("Searching for recommendations..."):
            #  Find matching movie title in dataset
            User_Movie_name_emmbedings = model.encode([Movie_name_input])
            movies_in_dataset_emmbedings = model.encode(data["Movie_Name"].astype(str).tolist())
            similarity = cosine_similarity(User_Movie_name_emmbedings, movies_in_dataset_emmbedings)[0]
            
            Index_of_Matching_movie = similarity.argmax()
            Movie_Name = data.iloc[Index_of_Matching_movie]["Movie_Name"]                 
            Movie_ID = data.iloc[Index_of_Matching_movie]["Movie_ID"]
            Movie_Genre = data.iloc[Index_of_Matching_movie]["Genre"]
            
            st.success(f"**Matched Movie:** {Movie_Name} | **Genre:** {Movie_Genre}")

            # Filter dataset by Genre and save/read matching genre file
            Genre_based_movie = data[data["Genre"] == Movie_Genre]
            Genre_based_movie.to_csv(f"{Movie_Genre}.csv", index=False)
            New_data = pd.read_csv(f"{Movie_Genre}.csv")

            # Step 3: Get matching movie description and encode
            Movie_description = New_data[New_data["Movie_ID"] == Movie_ID]

            Movie_Description_emmbedings = model.encode(Movie_description["Tokenised"].astype(str).tolist())
            Movies_in_dataset_emmbedings = model.encode(New_data["Tokenised"].astype(str).tolist())

            #Calculate description similarity scores
            similarity = cosine_similarity(
                Movie_Description_emmbedings,
                Movies_in_dataset_emmbedings
            )[0]

            sorted_index = similarity.argsort()[::-1]

            #  Output recommended movies in Streamlit
            st.subheader("Recommended Movies")
            for index in sorted_index[1:6]:
                st.write(f"{New_data.iloc[index]['Movie_Name']}")