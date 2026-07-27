import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("farm_data.csv")
print(df.isnull().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df=df.dropna()
df["Fertilizer_Used"]=df["Fertilizer_Used"].abs()
df["Yield"]=df["Yield"].abs()
df["Rainfall"]=df["Rainfall"].abs()
df.to_csv("farm_data.csv",index=False)
fig ,axis =plt.subplots(2,3,figsize=(12,6))
sns.scatterplot(
    data=df,
    x=df["Rainfall"],
    y=df["Yield"],
    hue=df["Crop"],
    ax=axis[0,0]
)
axis[0,0].set_title("Scatter Plot → Rainfall vs Yield (hue=Crop)")
# plt.show()
sns.lineplot(
    data=df.groupby("State",as_index=False)["Yield"].mean(),
    x="State",
    y="Yield",
    ax=axis[0,1]
)
axis[0,1].set_title("Line Plot → Average Yield by State")
axis[0,1].tick_params(axis="x", rotation=45)
# plt.show()
sns.barplot(
    data=df.groupby("Crop",as_index=False)["Yield"].mean(),
    x="Crop",
    y="Yield",
    ax=axis[0,2]
)
axis[0,2].tick_params(axis="x", rotation=45)
axis[0,2].set_title("Bar Plot → Average Yield by Crop")

# plt.show()
sns.boxplot(
    data=df,
    x="Crop",
    y="Yield",
    ax=axis[1,0]
)
axis[1,0].tick_params(axis="x", rotation=45)
axis[1,0].set_title("CBox Plot → Yield Distribution by Crop")
# plt.show()
sns.histplot(
    data=df,
    x="Rainfall",
    bins="auto",
    ax=axis[1,1]
)
plt.xticks(rotation=45)
axis[1,1].set_title("Histogram → Rainfall")
axis[1,2].axis("off")
plt.tight_layout()
plt.show()
print("Crop giving Highest Yield:")
print((df.groupby("Crop")["Yield"].max()).sort_values(ascending=False).head(1))
print("Highest Average production")
print((df.groupby("State")["Yield"].max()))

# Maharastra land gives highest yield
# Rice has highest yield Capacity among all
# Millet has lowest yield capacity
# Rice has highet Yield Distribution
# Rainfall Around 500-600 cm is most common