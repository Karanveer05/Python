import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("online_courses.csv")
print(df.isnull().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df=df.dropna()
df["Hours Studied"]=df["Hours Studied"].abs()
df["Quiz Score"]=df["Quiz Score"].abs()
df["Percentage"]=df["Percentage"].abs()
df.to_csv("online_courses.csv",index=False)
fig ,axis =plt.subplots(2,3,figsize=(12,6))
sns.scatterplot(
    data=df.groupby("Hours Studied",as_index=False)["Quiz Score"].mean(),
    x="Hours Studied",
    y="Quiz Score",
    hue=df["Device"],
    ax=axis[0,0]
)
axis[0,0].set_title("Scatter Plot → Hours Studied vs Quiz Score")
# plt.show()
sns.lineplot(
    data=df.groupby("Course",as_index=False)["Quiz Score"].mean(),
    x="Course",
    y="Quiz Score",
    ax=axis[0,1]
)
axis[0,1].set_title("Line Plot → Average Quiz Score by Course")
axis[0,1].tick_params(axis="x", rotation=45)
# plt.show()
sns.barplot(
    data=df.groupby("Course",as_index=False)["Percentage"].mean(),
    x="Course",
    y="Percentage",
    ax=axis[0,2]
)
axis[0,2].tick_params(axis="x", rotation=45)
axis[0,2].set_title("Bar Plot → Completion Percentage by Course")

# plt.show()
sns.boxplot(
    data=df,
    x="Device",
    y="Quiz Score",
    ax=axis[1,0]
)
axis[1,0].tick_params(axis="x", rotation=45)
axis[1,0].set_title("Box Plot → Quiz Score Distribution by Device")
# plt.show()
sns.histplot(
    data=df,
    x="Hours Studied",
    bins="auto",
    ax=axis[1,1]
)
plt.xticks(rotation=45)
axis[1,1].set_title("Histogram → Hours Studied")
axis[1,2].axis("off")
plt.tight_layout()
plt.show()
print("Course Having Highest Completion Rate :")
print((df.groupby("Course")["Percentage"].max()).sort_values(ascending=False).head(1))
print("Device Used Most :")
print((df["Device"].value_counts()).head(1))
print("Country Having Highest Average Quiz Score :")
print((df.groupby("Country")["Quiz Score"].max()).head(1))

#  Students who Have laptops score best in Quiz
# Quiz Score of Students in Java is High
# Score in Ai by Students is least
# ml and python courses are completed on time
# On an Average Student Studied Around 75 min