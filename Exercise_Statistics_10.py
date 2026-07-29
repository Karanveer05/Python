import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("daily.csv")

# create the dictonary with colums and values
statistical_types = {
    "Units": "Discrete",
    "Day": "Nominal",
    "Temprature": "Discrete",
    "City": "Nominal",
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
print("Mean Units is is :")
print(df["Units"].mean())
print("Median of Units is :")
print(df["Units"].median())
print(" mode of City is :")
print(df["City"].mode())
print("Range :")
print(df["Units"].var())
print("Standard Deviation :")
print(df["Units"].std())
print(df["Units"].max()-df["Units"].min())
print("IQR : ")
print(df["Units"].quantile(0.75)-df["Units"].quantile(0.25))
print(f"Outliers  :")
upperlimit=(df["Units"].quantile(0.25))+1.5*(df["Units"].quantile(0.75)-df["Units"].quantile(0.25))
Lowerlimit=(df["Units"].quantile(0.75))-1.5*(df["Units"].quantile(0.75)-df["Units"].quantile(0.25))
outlier=df[( df["Units"] > upperlimit )]
print(outlier)
# in winter less electricty consumed as compared that of winter
#median in better because it tell us the median values as it give us the mid values