import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read the CSV file
df = pd.read_csv("Nasa.csv")

# create the dictonary with colums and values
statistical_types = {
    "Reading_ID": "Discrete",
    "Temperature": "Discrete",
    "Pressure": "Continuous",
    "Battery_Level": "Discrete",
    "Tarrain_Type": "Nominal",
    "Signal_Strength": "Discrete",

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
print("Mean of Temperature  is :")
print(df["Temperature"].mean())
print("Median of Pressure is :")
print(df["Pressure"].median())
print(" mode of Battery_Level is :")
print(df["Battery_Level"].mode())
print("Variance")
print(df["Temperature"].var())
print("Standard Deviation :")
print(df["Temperature"].std())
print("IQR : ")
print(df["Pressure"].quantile(0.75)-df["Pressure"].quantile(0.25))
print(f"Outliers  :")
print(f"quantiles 25 % {df['Temperature'].quantile(0.25)}")
print(f"quantiles 50 % {df['Temperature'].quantile(0.50)}")
print(f"quantiles 75 % {df['Temperature'].quantile(0.75)}")
upperlimit=(df["Temperature"].quantile(0.25))+1.5*(df["Temperature"].quantile(0.75)-df["Temperature"].quantile(0.25))
Lowerlimit=(df["Temperature"].quantile(0.75))-1.5*(df["Temperature"].quantile(0.75)-df["Temperature"].quantile(0.25))
outlier=df[( df["Temperature"] > upperlimit )]
print(outlier)
print("Top 10 percent Influencers")
print(df[df["Pressure"]>np.percentile(df["Pressure"],90)])
print("90th percentile ")
print(np.percentile(df["Temperature"],90))
plt.boxplot(df["Pressure"])
plt.title("BOX PLOT")
plt.show()