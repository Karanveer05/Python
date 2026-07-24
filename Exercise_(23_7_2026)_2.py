import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Retail_Sales.csv")
df["FinalAmount"]=(df["Quantity"] *df["Price"])-df["Discount"]
df["Quantity"]=df["Quantity"].abs()
df["Price"]=df["Price"].abs()
df=df.drop_duplicates()
# df=df
# df=df.dropna()
# df["Quantity"]=df["Quantity"].fillna(df["Quantity"].mean())
df=df.dropna()
df.to_csv("Retail_Sales.csv",index=False)
# print("-"*70)
print(df.isnull().sum())
print("Highest Revenue Product is ")
print(df.sort_values(by="FinalAmount",ascending=False).head(1))
print("-"*70)
print("Lowest Revenue Product is ")
print(df.sort_values(by="FinalAmount",ascending=True).head(1))
print("-"*70)
print("Average Order Value by Product is ")
print((df.groupby("Product")["Quantity"].mean()).sort_values(ascending=False))
print("-"*70)
print("City wit highest sales : ")
print((df.groupby("City")["FinalAmount"].sum()).sort_values(ascending=False).head(1))
print("-"*70)

plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
Bar_Chart=df.groupby("Category")["FinalAmount"].sum()
plt.bar(Bar_Chart.index,Bar_Chart)
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45,ha="right")
plt.title("Bar chart → Average Salary by Department.")
plt.subplot(1,3,2)
Pie_chart=df.groupby("City")["Quantity"].sum()
plt.pie(Pie_chart,labels=Pie_chart.index,autopct="%1.1f%%")
plt.title("City-wise order percentage (Pie Chart).")
plt.subplot(1,3,3)
plt.hist(df["FinalAmount"],bins="auto")
plt.title("Histogram → Sales Distribution.")
plt.tight_layout()
plt.show()
#Electronic items are highly purchased
#lucknow is largest source of revenue in sales
#people  highly purchase products around 0-$200,000
# Hyderabad has least profatible market for sales
#Groceries are least ordered by people