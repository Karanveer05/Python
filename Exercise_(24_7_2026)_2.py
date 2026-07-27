import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("ev_charging.csv")
print(df.isnull().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df=df.dropna()
df["Charging_Time"]=df["Charging_Time"].abs()
df["Energy_Consumed"]=df["Energy_Consumed"].abs()
df.to_csv("ev_charging.csv",index=False)
fig ,axis =plt.subplots(2,3,figsize=(12,6))
sns.scatterplot(
    data=df,
    x=df["Charging_Time"],
    y=df["Energy_Consumed"],
    hue=df["Charging_Type"],
    ax=axis[0,0]
)
axis[0,0].set_title("Scatter Plot → Charging Time vs Energy Consumed")
# plt.show()
sns.lineplot(
    data=df.groupby("City",as_index=False)["Energy_Consumed"].mean(),
    x="City",
    y="Energy_Consumed",
    ax=axis[0,1]
)
axis[0,1].set_title("Line Plot → Average Energy Consumed by City")
axis[0,1].tick_params(axis="x", rotation=45)
# plt.show()
sns.barplot(
    data=df.groupby("City",as_index=False)["Cost"].mean(),
    x="City",
    y="Cost",
    ax=axis[0,2]
)
axis[0,2].tick_params(axis="x", rotation=45)
axis[0,2].set_title("Total Revenue by City")

# plt.show()
sns.boxplot(
    data=df,
    x="Charging_Type",
    y="Cost",
    ax=axis[1,0]
)
plt.xticks(rotation=45)
axis[1,0].set_title("Cost Distribution by Charging Type")
# plt.show()
sns.histplot(
    data=df,
    x="Charging_Time",
    bins="auto",
    ax=axis[1,1]
)
plt.xticks(rotation=45)
axis[1,1].set_title("Charging Type")
axis[1,2].axis("off")
plt.tight_layout()
plt.show()
print("City generating max Revenue :")
print((df.groupby("City")["Cost"].sum()).sort_values(ascending=False).head(1))
print("Average Charging Time by vehicle :")
print((df.groupby("Vehicle_Type")["Charging_Time"].mean()))
print("Most Common Charging Type ")
print(df["Charging_Type"].value_counts().head(1))

# Energy consumed by scooty is directly propotional to the time taken to charge 
# Mumbai city comsumed high energy
# Mumbai generates high energy
# fast charging vehicles consumes high energy
# most of scooty charge time is 60 to 70 km