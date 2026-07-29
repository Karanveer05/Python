import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("Animal.csv")

# create the dictonary with colums and values
statistical_types = {
    "Animal": "Nominal",
    "Species": "Nominal",
    "Forest": "Nominal",
    "Age": "Discrete",
    "Weight": "Continuous",
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
print("Mean of Weight  is :")
print(df["Weight"].mean())
print("Median of Weight is :")
print(df["Weight"].median())
print(" mode of species is :")
print(df["Species"].mode())
print("Range :")
print(df["Weight"].max()-df["Weight"].min())
print("Variance")
print(df["Weight"].var())
print("Standard Deviation :")
print(df["Weight"].std())
print("IQR : ")
print(df["Weight"].quantile(0.75)-df["Weight"].quantile(0.25))
print(f"Outliers  :")
print(f"quantiles 25 % {df['Weight'].quantile(0.25)}")
print(f"quantiles 50 % {df['Weight'].quantile(0.50)}")
print(f"quantiles 75 % {df['Weight'].quantile(0.75)}")
upperlimit=(df["Weight"].quantile(0.25))+1.5*(df["Weight"].quantile(0.75)-df["Weight"].quantile(0.25))
Lowerlimit=(df["Weight"].quantile(0.75))-1.5*(df["Weight"].quantile(0.75)-df["Weight"].quantile(0.25))
outlier=df[( df["Weight"] > upperlimit )]
print(outlier)
print("Heavy Animal is :")
print(df[df["Weight"]==df["Weight"].max()])