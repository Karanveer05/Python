import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("Placement.csv")

# create the dictonary with colums and values
statistical_types = {
    "Student": "Nominal",
    "Branch": "Nominal",
    "Package": "Continuous",
    "CGPA": "Continuous",
    "Interview_Score": "Continuous",
    "Company": "Nominal",
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

print(result[(result["Type"]=="Continuous")|(result["Type"]=="discreate")])
print("Mean Package is :")
print(df["Package"].mean())
print("Median of Package is :")
print(df["Package"].median())
print(" mode of Package is :")
print(df["Package"].mode())
print("Range :")
print(df["Package"].max()-df["Package"].min())
print("Variance :")
print(df["Package"].var())
print("Standard Deviation :")
print(df["Package"].std())
print(f"Salary Qunatile (Q1) : {df['Package'].quantile(0.25)}")
print(f"Salary Qunatile (Q2) : {df['Package'].quantile(0.50)}")
print(f"Salary Qunatile (Q3) : {df['Package'].quantile(0.75)}")
print("IQR :")
print(df["Package"].quantile(0.75)-df["Package"].quantile(0.25))
print(f"Outliers  :")
upperlimit=df["Package"].max()
Lowerlimit=df["Package"].min()
outlier=df[( df["Package"] < upperlimit )|( df["Package"] > Lowerlimit )]
print(outlier)
print("80th percentile of salary package is ")
print(np.percentile(df["Package"],80))
print("High Salary :")
print(df[df["Package"]==df["Package"].max()])