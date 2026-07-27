import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("space_missions.csv")
print(df.isnull().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df=df.dropna()
df["Cost"]=df["Cost"].abs()
df["Payload_Weight"]=df["Payload_Weight"].abs()
df.to_csv("space_missions.csv",index=False)
fig ,axis =plt.subplots(2,3,figsize=(12,6))                 # plt.figure(figsize=(12,6))
sns.scatterplot(                                            #plt.subplot(Rows,colums,position)
    data=df,
    x=df["Cost"],
    y=df["Payload_Weight"],
    hue=df["Success"],
    ax=axis[0,0]
)
axis[0,0].set_title("Scatter Plot → Mission Cost vs Payload Weight")        #plt.title(" ---------")
# plt.show()
lineplot_graph=df["Launch Year"].value_counts()
sns.lineplot(
    # data=lineplot_graph,
    x=lineplot_graph.index,
    y=lineplot_graph,
    ax=axis[0,1]
)
axis[0,1].set_title("Line Plot → Missions Launched Per Year")
axis[0,1].tick_params(axis="x", rotation=45)                         # plt.xticks(rotation=45,ha="right/left")
# # plt.show()
sns.barplot(
    data=df.groupby("Country",as_index=False)["Cost"].mean(),
    x="Country",
    y="Cost",
    ax=axis[0,2]
)
axis[0,2].tick_params(axis="x", rotation=45)
axis[0,2].set_title("Bar Plot → Average Mission Cost by Country")

# plt.show()
sns.boxplot(
    data=df,
    x="Rocket Type",
    y="Payload_Weight",
    ax=axis[1,0]
)
axis[1,0].tick_params(axis="x", rotation=45)
axis[1,0].set_title("Box Plot → Payload Distribution by Rocket Type")
# plt.show()
sns.histplot(
    data=df,
    x="Cost",
    bins="auto",
    ax=axis[1,1]
)
axis[1,1].tick_params(axis="x",rotation=45)
axis[1,1].set_title("Histogram → Mission Cost")
axis[1,2].axis("off")
plt.tight_layout()
plt.show()
print("Country having highest average mission cost :")
print((df.groupby("Country")["Cost"].mean()).sort_values(ascending=False).head(1))
print("Rocket Carries the Heviest Payload :")
print((df.groupby("Rocket Type")["Payload_Weight"].max()).head(1))
print("Mission Sucess Rate for Each Country")
print((df["Success"]=="Yes").groupby(df["Country"]).mean()*100)
#In 2000,2020 high number of missionns take place
# Japan has high budget for space missions
# March 5 rocket is highly fexxible for payload weight
# In 2015 Less no of mission take place 
# 