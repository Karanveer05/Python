import pandas as pd

# Read the CSV file
df = pd.read_csv("athletes.csv")

# create the dictonary with colums and values
statistical_types = {
    "Athlete": "Nominal",
    "Country": "Nominal",
    "Sport": "Nominal",
    "Age": "Discrete",
    "Height": "Continuous",
    "Weight": "Continuous",
    "Medal": "Discrete",
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
print("Mean Age is :")
print(df["Age"].mean())
print("Median Height is :")
print(df["Height"].median())
print("  mode of Sport is :")
print(df["Sport"].mode())
print("Range of weights :")
print(df["Weight"].max()-df["Weight"].min())
print("Variance  of heights:")
print(df["Height"].var())
print("Standard Deviation of ages :")
print(df["Age"].std())
print(f"Salary Qunatile (Q1) : {df['Medal'].quantile(0.25)}")
print(f"Salary Qunatile (Q2) : {df['Medal'].quantile(0.50)}")
print(f"Salary Qunatile (Q3) : {df['Medal'].quantile(0.75)}")
print("IQR :")
print(df["Medal"].quantile(0.75)-df["Medal"].quantile(0.25))
print(f" Athletes with high medals :")
print(df[df["Medal"]==df["Medal"].max()])