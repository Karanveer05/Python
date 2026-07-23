import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Movie": [
        "Pushpa", "RRR", "KGF Chapter 2", "Dangal", "3 Idiots",
        "Bahubali", "Drishyam", "Jawan", "Pathaan", "Animal",
        "Leo", "Vikram", None,None, "Chhichhore",
        "PK", "Gadar 2", "Brahmastra", "Shershaah", "Sooryavanshi",
        "Kalki 2898 AD", "Stree 2", "Maharaja", "Thunivu", "Pushpa 2"
    ],

    "Genre": [
        "Action", "Action", "Action", "Sports", "Comedy",
        "Action", None, "Action", "Action", "Action",
        "Action", "Thriller", "Drama", None, "Comedy",
        "Comedy", "Action", "Fantasy", "War", "Action",
        "Sci-Fi",None, "Thriller", "Action", "Action"
    ],

    "Rating": [
        8.2, 8.8, 8.4, 8.5, 8.4,
        8.1, 8.3, 7.8, 7.6, 7.9,
        7.8, 8.4, 8.3, 8.5, 8.3,
        8.1, 6.9, None, 8.4, 6.8,
        8.3, 8.0, 8.6, 7.5, 8.7
    ],

    "Duration": [
        2.9, 3.0, 2.8, 2.7, 2.9,
        2.6, 2.4, 2.8, 2.6, 3.2,
        2.7, 2.9,None, 2.7, 2.5,
        2.4, 2.8, 2.9, 2.3, 2.4,
        3.0, 2.4, 2.3, 2.4, 3.2
    ],

    "Year": [
        2021, 2022, 2022, 2016, 2009,
        2015,None, 2023, 2023, 2023,
        2023, 2022, 2022, 2022, 2019,
        2014, 2023, 2022, 2021, 2021,
        2024, 2024, 2024, 2023, None
    ],

    "Language": [
        "Telugu", "Telugu", "Kannada", None, "Hindi",
        "Telugu", "Hindi", "Hindi", "Hindi", "Hindi",
        "Tamil",None, "Kannada", "Telugu", "Hindi",
        "Hindi", "Hindi", "Hindi", "Hindi", "Hindi",
        "Telugu", "Hindi", "Tamil", "Tamil", "Telugu"
    ],

    "Views": [
        350, 420, 390, 7, 280,
        70, 210,None, 240, 280,
        250, 30, 220, 80, 170,
        290, 190, 60, 210, 150,
        10, None, 140, 60, 450
    ]
}         # data generated  from model

df = pd.DataFrame(data)
df.to_csv("Movies.csv", index=False)
print('-'*50)
print(df.isnull())
print('-'*50)
df = df.dropna()
print(df.isnull())
print('-'*50)
print("Movies After 2020 :")
print(df[df["Year"]>2020])
print('-'*50)
print("Rating Greater than 8:")
print(df[df["Rating"]>8])
print('-'*50)
print("View Greater than 100 MIllion :")
print(df[df["Views"]>100])
print('-'*50)
print(df.describe())
plt.figure(figsize=(12,6))
print('-'*50)
filtered_movies=df[
    (df["Rating"] > 8) & 
    (df["Year"] > 2020) & 
    (df["Views"]>100) &
    (df["Genre"].str.upper()=="ACTION")           
]
print(filtered_movies)
filtered_movies.to_csv("Top Movies.csv",index=False)
plt.subplot(2,3,1)
plt.plot(df["Movie"].index,df["Views"],marker="o")
plt.xlabel("Movie")
plt.ylabel("Views")
plt.title(" Line Plot → Views")
plt.grid(True)

plt.subplot(2,3,2)
plt.bar(df["Movie"].index,df["Rating"])
plt.xlabel("Movie")
plt.ylabel("Rating")
plt.title(" Bar Chart → Movie Ratings.")
plt.grid(True)

plt.subplot(2,3,3)
plt.hist(df["Views"],bins="auto")
plt.ylabel("Views")
plt.title(" Histogram → Views Distribution.")
plt.grid(True)

plt.subplot(2,3,4)
count=df["Genre"].value_counts()
plt.pie(count,labels=count.index,autopct='%1.f%%')
plt.title("  Pie Chart → Genre Distribution.")

plt.subplot(2,3,5)
plt.scatter(df["Duration"],df["Rating"])
plt.xlabel("Duration")
plt.ylabel("Rating")
plt.title("Scatter Plot → Duration vs Rating.")
plt.grid(True)

plt.tight_layout()
plt.show()
