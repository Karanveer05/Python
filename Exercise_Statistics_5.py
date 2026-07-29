import pandas as pd

# Read the CSV file
df = pd.read_csv("household.csv")

# create the dictonary with colums and values
statistical_types = {
    "House_ID": "Nominal",
    "Family_Size": "Discrete",
    "Daily_Water_Usage": "Continuous",
    "Area": "Nominal",
    "Income_Group": "Nominal",
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
print("Mean Daily_Water_Usage is :")
print(df["Daily_Water_Usage"].mean())
print("Median of Daily_Water_Usage is :")
print(df["Daily_Water_Usage"].median())
print(" mode of Daily_Water_Usage is :")
print(df["Daily_Water_Usage"].mode())
print("Range :")
print(df["Daily_Water_Usage"].max()-df["Daily_Water_Usage"].min())
print("Variance :")
print(df["Daily_Water_Usage"].var())
print("Standard Deviation :")
print(df["Daily_Water_Usage"].std())
print(f"Salary Qunatile (Q1) : {df['Daily_Water_Usage'].quantile(0.25)}")
print(f"Salary Qunatile (Q2) : {df['Daily_Water_Usage'].quantile(0.50)}")
print(f"Salary Qunatile (Q3) : {df['Daily_Water_Usage'].quantile(0.75)}")
print("IQR :")
print(df["Daily_Water_Usage"].quantile(0.75)-df["Daily_Water_Usage"].quantile(0.25))
print(f"Outliers  :")
upperlimit=df["Daily_Water_Usage"].max()
Lowerlimit=df["Daily_Water_Usage"].min()
outlier=df[( df["Daily_Water_Usage"] < upperlimit )|( df["Daily_Water_Usage"] > Lowerlimit )]
print(outlier)
print("House use Max water :")
print(df[df["Daily_Water_Usage"]==df["Daily_Water_Usage"].max()])