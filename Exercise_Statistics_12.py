import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("cryptocurrencies.csv")

# create the dictonary with colums and values
statistical_types = {
    "Coin": "Nominal",
    "Category": "Nominal",
    "Market_Cap": "Discrete",
    "Daily_Return": "Continuous",
    "Trading_Volume": "Discrete",
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
print("Mean of return value  is :")
print(df["Daily_Return"].mean())
print("Median of Market_Cap is :")
print(df["Market_Cap"].median())
print(" mode of Category is :")
print(df["Category"].mode())
print("Range :")
print(df["Daily_Return"].max()-df["Daily_Return"].min())
print("Variance")
print(df["Daily_Return"].var())
print("Standard Deviation :")
print(df["Daily_Return"].std())
print("IQR : ")
print(df["Daily_Return"].quantile(0.75)-df["Daily_Return"].quantile(0.25))
print(f"Outliers  :")
print(f"quantiles 25 % {df['Daily_Return'].quantile(0.25)}")
print(f"quantiles 50 % {df['Daily_Return'].quantile(0.50)}")
print(f"quantiles 75 % {df['Daily_Return'].quantile(0.75)}")
upperlimit=(df["Daily_Return"].quantile(0.25))+1.5*(df["Daily_Return"].quantile(0.75)-df["Daily_Return"].quantile(0.25))
Lowerlimit=(df["Daily_Return"].quantile(0.75))-1.5*(df["Daily_Return"].quantile(0.75)-df["Daily_Return"].quantile(0.25))
outlier=df[( df["Daily_Return"] > upperlimit )]
print(outlier)
#as the returns depend upon the market cap so they are highly volatie