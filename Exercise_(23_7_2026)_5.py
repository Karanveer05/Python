import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("ecommerce_dataset_records.csv")
df=df.drop_duplicates()
df=df.dropna()
print(df.isnull().sum())          
print(df.duplicated().sum())
df.to_csv("ecommerce_dataset_records.csv",index=False)
print(df)
print("-"*80)
print(df.head(1))
print("-"*80)
print(df.tail(1))
print("-"*80)
print(df.info())
print("-"*80)
print(df.describe())
print("-"*80)
print(df["ID"].value_counts())
print(df.value_counts(["ID","Quantity"]))
print("-"*80)
print(df.sort_values(["Quantity","Amount"],ascending=[True,False]))
print("-"*80)
print(df.groupby("Product")["Amount"].max())
print("-"*80)
print(df.groupby("Quantity")["Amount"].min())
print("-"*80)
print(df.groupby("Payment")["Amount"].sum())
plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
Bar_graph=df["Payment"].value_counts()
plt.bar(Bar_graph.index,Bar_graph)
plt.title("Payment-Bar graph")
plt.xlabel("Payment type")
plt.ylabel("No of Payments")

plt.subplot(2,2,2)
Pie_Chart=df.groupby("Product")["Quantity"].sum()
plt.pie(Pie_Chart,labels=Pie_Chart.index,autopct="%1.1f%%")
plt.title("Pie Chart -  total Quantity")

plt.subplot(2,2,3)

plt.hist(df["Amount"],bins="auto")
plt.title("Histogram of amount")
plt.tight_layout()
plt.show()

# Data Set Overview :
#  data has null and duplicates value 
#  
# 
# cleaning steps:
# 
# find the duplicates,null values using df.isnull(),df.duplicated()
# assign the average value to the null spaces by df["column"]=df["colums"].fillna(df["column"].mean())   ?? if you want then do it if not go to next step
#  use mean(),max(),min()or fillna(Value)
# 
# now remove the duplicates rows
# df=df.dropna()   remove null valued rows
# df=df.drop_duplicates()  // remove duplicate rows
# 
# comit it to csv using
# df.to_csv("filename",index=False)
# 
# Key Statistics:
# clean the data properly
# comit the change to files
# check the changeshas been commited the data
# 
# visualization
# easy fetch the important information 
# easy to understand as user friendly
# 
# Business insights
# Most people use online mode for payment
#mouse is highly purchased device
#people purchased products cost arround 15000-25000
#laptop and keyword are least purchased by people
# Headphone is costly