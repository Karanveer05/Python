import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("Airline.csv")

# create the dictonary with colums and values
statistical_types = {
    "Flight": "Nominal",
    "Airline": "Nominal",
    "Delay_Minutes": "Discrete",
    "Destination": "Nominal",
    "Ticket_Class": "Nominal",
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
print("Mean Delay_Minutes is is :")
print(df["Delay_Minutes"].mean())
print("Median of Delay_Minutes is :")
print(df["Delay_Minutes"].median())
print(" mode of Delay_Minutes is :")
print(df["Delay_Minutes"].mode())
print("Range :")
print(df["Delay_Minutes"].var())
print("Standard Deviation :")
print(df["Delay_Minutes"].std())
print(df["Delay_Minutes"].max()-df["Delay_Minutes"].min())
print("IQR : ")
print(df["Delay_Minutes"].quantile(0.75)-df["Delay_Minutes"].quantile(0.25))
print(f"Outliers  :")
print(f"quantiles 25 % {df['Delay_Minutes'].quantile(0.25)}")
print(f"quantiles 50 % {df['Delay_Minutes'].quantile(0.50)}")
print(f"quantiles 75 % {df['Delay_Minutes'].quantile(0.75)}")
upperlimit=(df["Delay_Minutes"].quantile(0.25))+1.5*(df["Delay_Minutes"].quantile(0.75)-df["Delay_Minutes"].quantile(0.25))
Lowerlimit=(df["Delay_Minutes"].quantile(0.75))-1.5*(df["Delay_Minutes"].quantile(0.75)-df["Delay_Minutes"].quantile(0.25))
outlier=df[( df["Delay_Minutes"] > upperlimit )]
print(outlier)
print(" max Delayed Flight :")
print(df[df["Delay_Minutes"]==df["Delay_Minutes"].max()])