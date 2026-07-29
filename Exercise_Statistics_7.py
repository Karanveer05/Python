import pandas as pd
import numpy as np
# Read the CSV file
df = pd.read_csv("Ticket.csv")

# create the dictonary with colums and values
statistical_types = {
    "Booking_ID": "Discrete",
    "Movie": "Nominal",
    "Seat_Type": "Nominal",
    "Ticket_Price": "Discrete",
    "Number_of_Tickets": "Discrete",
    "Booking_Day": "Nominal",

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
print("Mean Ticket_Price is :")
print(df["Ticket_Price"].mean())
print("Median of Ticket_Price is :")
print(df["Ticket_Price"].median())
print(" mode of Seat_Type is :")
print(df["Seat_Type"].mode())
print("Range :")
print(df["Ticket_Price"].max()-df["Ticket_Price"].min())
print("Variance :")
print(df["Ticket_Price"].var())
print("Standard Deviation :")
print(df["Ticket_Price"].std())
print(f"Ticket Price Qunatile (Q1) : {df['Ticket_Price'].quantile(0.25)}")
print(f"Ticket Price Qunatile (Q2) : {df['Ticket_Price'].quantile(0.50)}")
print(f"Ticket Price Qunatile (Q3) : {df['Ticket_Price'].quantile(0.75)}")
print("IQR :")
print(df["Ticket_Price"].quantile(0.75)-df["Ticket_Price"].quantile(0.25))
print(f"Outliers  :")
upperlimit=df["Ticket_Price"].max()
Lowerlimit=df["Ticket_Price"].min()
outlier=df[( df["Ticket_Price"] < upperlimit )|( df["Ticket_Price"] > Lowerlimit )]
print(outlier)
