import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("Delivery.csv")

# create the dictonary with colums and values
statistical_types = {
    "Delivery_ID": "Discrete",
    "Restaurant": "Nominal",
    "Distance": "Continuous",
    "Delivery_Time": "Continuous",
    "Delivery_Partner": "Nominal",
    "Rating": "Continuous",
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
print("Mean Delivery_Time is is :")
print(df["Delivery_Time"].mean())
print("Median of Distance is :")
print(df["Distance"].median())
print(" mode of Restaurant is :")
print(df["Restaurant"].mode())
print("Range :")
print(df["Delivery_Time"].max()-df["Delivery_Time"].min())
print("IQR :")
print(df["Delivery_Time"].quantile(0.75)-df["Delivery_Time"].quantile(0.25))
print(f"Outliers  :")
upperlimit=(df["Delivery_Time"].quantile(0.25))+1.5*(df["Delivery_Time"].quantile(0.75)-df["Delivery_Time"].quantile(0.25))
Lowerlimit=(df["Delivery_Time"].quantile(0.75))-1.5*(df["Delivery_Time"].quantile(0.75)-df["Delivery_Time"].quantile(0.25))
outlier=df[( df["Delivery_Time"] > upperlimit )]
print(outlier)
#median in better because it tell us the median values as it give us the mid values