import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("airport_traffic.csv")
print(df.isnull().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df=df.dropna()
df["Ticket_Price"]=df["Ticket_Price"].abs()
df["Delay_Minutes"]=df["Delay_Minutes"].abs()
df.to_csv("airport_traffic.csv",index=False)
fig ,axis =plt.subplots(2,3,figsize=(12,6))
sns.scatterplot(
    data=df,
    x=df["Ticket_Price"],
    y=df["Flight_Duration"],
    hue=df["Travel_Class"],
     ax=axis[0,0]
)
axis[0,0].set_title("Ticket Price vs Flight Duration")
# plt.show()
sns.lineplot(
    data=df.groupby("Airline",as_index=False)["Ticket_Price"].mean(),
    x="Airline",
    y="Ticket_Price",
    ax=axis[0,1]
)
axis[0,1].set_title("Average Ticket Price by Airline")
# plt.show()
sns.barplot(
    data=df.groupby("Airline",as_index=False)["Delay_Minutes"].mean(),
    x="Airline",
    y="Delay_Minutes",
    ax=axis[0,2]
)
axis[0,2].set_title("Average Delay by Airline")

# plt.show()
sns.boxplot(
    data=df,
    x="Travel_Class",
    y="Delay_Minutes",
    ax=axis[1,0]
)
axis[1,0].set_title("Delay by Travel Class")
# plt.show()
sns.histplot(
    data=df,
    x="Ticket_Price",
    bins=30,
    ax=axis[1,1]
)
axis[1,1].set_title("Ticket Price Distribution")
axis[1,2].axis("off")
plt.tight_layout()
plt.show()
print("Airline Charges Highest Average Price :")
print((df.groupby("Airline")["Ticket_Price"].mean()).sort_values(ascending=False).head(1))
print()
print("Travel Classs Having longest delays : ")
print((df.groupby("Travel_Class")["Delay_Minutes"].mean()).sort_values(ascending=False).head(1))
print()
print("Destination Recieves highest Passengers : ")
print(df["Destination_City"].value_counts().head(1))
print()

# Akasa Air line Has Less Delay minutes as compared to that of others
# Akasa Air line has lowest average Tickert price 
# ticket price i economy is directly propotinal to flight duration
# high no of percentage pay 5000,9000 for ticket
# Economy class face less Delay Flights
