import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("Influencer.csv")

# create the dictonary with colums and values
statistical_types = {
    "Influencer": "Nominal",
    "Platform": "Nominal",
    "Followers": "Discrete",
    "Category": "Nominal",
    "Engagement_Rate": "Continuous",
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
print("Mean of Followers  is :")
print(df["Followers"].mean())
print("Median of Engagement_Rate is :")
print(df["Engagement_Rate"].median())
print(" mode of Platform is :")
print(df["Platform"].mode())
print("Variance")
print(df["Followers"].var())
print("Standard Deviation :")
print(df["Followers"].std())
print("IQR : ")
print(df["Followers"].quantile(0.75)-df["Followers"].quantile(0.25))
print(f"Outliers  :")
print(f"quantiles 25 % {df['Followers'].quantile(0.25)}")
print(f"quantiles 50 % {df['Followers'].quantile(0.50)}")
print(f"quantiles 75 % {df['Followers'].quantile(0.75)}")
upperlimit=(df["Followers"].quantile(0.25))+1.5*(df["Followers"].quantile(0.75)-df["Followers"].quantile(0.25))
Lowerlimit=(df["Followers"].quantile(0.75))-1.5*(df["Followers"].quantile(0.75)-df["Followers"].quantile(0.25))
outlier=df[( df["Followers"] > upperlimit )]
print(outlier)
print("Top 10 percent Influencers")
print(df[df["Engagement_Rate"]>np.percentile(df["Engagement_Rate"],90)])