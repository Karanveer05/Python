import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Country": ["India", "USA", "Japan", "China", "Canada"],
    "Population": [1400, 331, 125, 1412, 38],
    "Literacy Rate": [77, 99, 99, 97, None],
    "GDP": [3.7, 25.4, 4.2, 17.9, None],
    "Continent": ["Asia", "North America", "Asia", "Asia", "North America"]
}

df = pd.DataFrame(data)

print("World Population Data")
print(df)

print("-" * 50)
print("Countries with Population Greater than 100 Million")
print(df[df["Population"] > 100])

print("-" * 50)
print("Countries with Literacy Rate Greater than 90%")
print(df[df["Literacy Rate"] > 90])

print("-" * 50)
print("Country with Highest GDP")
print(df[df["GDP"] == df["GDP"].max()])

print("-" * 50)
print("Country with Lowest GDP")
print(df[df["GDP"] == df["GDP"].min()])

print("-" * 50)
print("Average GDP")
print(df["GDP"].mean())

print("-" * 50)
print("Data After Filling Missing Values")

df = df.fillna(0)
print(df)

df.to_csv("world_population_cleaned.csv", index=False)
print("Cleaned data saved successfully.")

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.bar(df["Country"], df["GDP"])
plt.xlabel("Country")
plt.ylabel("GDP")
plt.title("Country vs GDP")
plt.grid(True)

plt.subplot(2, 2, 2)

plt.pie(df["Continent"].value_counts(),labels=df["Continent"],autopct="%1.1f%%")
plt.title("Continent Distribution")

plt.subplot(2, 2, 3)
plt.scatter(df["Population"], df["GDP"])
plt.xlabel("Population (Million)")
plt.ylabel("GDP")
plt.title("Population vs GDP")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.hist(df["Literacy Rate"], bins="auto")
plt.xlabel("Literacy Rate")
plt.ylabel("Number of Countries")
plt.title("Literacy Rate Distribution")
plt.grid(True)

plt.tight_layout()
plt.show()