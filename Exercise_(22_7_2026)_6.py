import pandas as pd
import matplotlib.pyplot as plt
data ={
 "Movie":['A','B','C'],
 "Genre":["Comdy","Action","horror"],
 "Duration":[2,1.4,3],
 "Rating":[2,9,7],
 "Year":[2023,2004,2015],
}
df=pd.DataFrame(data)
print(df)
print("Movies After 2020 :")
print(df[df["Year"]>2020])
print("Rating Greater than 8:")
print(df[df["Rating"]>8])
print("Longest Movie :")
print(df[df["Duration"]==df["Duration"].max()])
print("shortest Movie :")
print(df[df["Duration"]==df["Duration"].min()])
print("Average Duration   :")
print(f"{df['Duration'].mean()} hours")
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.bar(df["Movie"],df["Rating"])
plt.xlabel("Movie")
plt.ylabel("Rating")
plt.title(" Bar Chart → Movie Ratings.")
plt.grid(True)
plt.subplot(2,2,2)
plt.hist(df["Rating"],bins="auto")
plt.ylabel("Ratings")
plt.title("  Histogram → Ratings.")
plt.grid(True)
plt.subplot(2,2,3)
plt.pie(df["Rating"],labels=df["Genre"],autopct='%1.f%%')
plt.title("  Pie Chart → Genre Distribution.")
plt.tight_layout()
plt.show()
