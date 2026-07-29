import pandas as pd

# Read the CSV file
df = pd.read_csv("Music.csv")

# create the dictonary with colums and values
statistical_types = {
    "Song": "Nominal",
    "Artist": "Nominal",
    "Genre": "Nominal",
    "Duration": "Continuous",
    "Streams": "Discrete",
    "Release_Year": "Discrete",
}
print()
# Create a result DataFrame
result=pd.DataFrame({
    " Data Type":df.dtypes,
    "Type":[
      statistical_types.get(column,"Unknown")
      for column in df.columns
    ]
    
})

print(result)
print("Mean Streams is :")
print(df["Streams"].mean())
print("Median of Duration is :")
print(df["Duration"].median())
print("  mode of Genre is :")
print(df["Genre"].mode())
print("Range :")
print(df["Streams"].max()-df["Streams"].min())
print("Variance :")
print(df["Streams"].var())
print("Standard Deviation :")
print(df["Streams"].std())
print(f"Salary Qunatile (Q1) : {df['Streams'].quantile(0.25)}")
print(f"Salary Qunatile (Q2) : {df['Streams'].quantile(0.50)}")
print(f"Salary Qunatile (Q3) : {df['Streams'].quantile(0.75)}")
print("IQR :")
print(df["Streams"].quantile(0.75)-df["Streams"].quantile(0.25))
print(f"Outliers  :")
upperlimit=df["Streams"].max()
Lowerlimit=df["Streams"].min()
outlier=df[( df["Streams"] < upperlimit )|( df["Streams"] > Lowerlimit )]
print(outlier)