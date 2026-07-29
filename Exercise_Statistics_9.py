import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("hotel_bookings.csv")

# create the dictonary with colums and values
statistical_types = {
    "Booking_ID": "Discrete",
    "Stay_Days": "Discrete",
    "Room_Price": "Continuous",
    "Guests": "Discrete",
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
print("Mean Room_Price is is :")
print(df["Room_Price"].mean())
print("Median of Room_Price is :")
print(df["Room_Price"].median())
print(" mode of Room_Price is :")
print(df["Room_Price"].mode())
print("Range :")
print(df["Room_Price"].var())
print("Standard Deviation :")
print(df["Room_Price"].std())
print(df["Room_Price"].max()-df["Room_Price"].min())
print("IQR : ")
print(df["Room_Price"].quantile(0.75)-df["Room_Price"].quantile(0.25))
print(f"Outliers  :")
upperlimit=(df["Room_Price"].quantile(0.25))+1.5*(df["Room_Price"].quantile(0.75)-df["Room_Price"].quantile(0.25))
Lowerlimit=(df["Room_Price"].quantile(0.75))-1.5*(df["Room_Price"].quantile(0.75)-df["Room_Price"].quantile(0.25))
outlier=df[( df["Room_Price"] > upperlimit )]
print(outlier)
print("20th percentile")
print(np.percentile(df["Room_Price"],20))
print("50th percentile")
print(np.percentile(df["Room_Price"],50))
print("95th percentile")
print(np.percentile(df["Room_Price"],95))
#median in better because it tell us the median values as it give us the mid values