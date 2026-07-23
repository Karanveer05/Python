
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Number=int(input("Enter the number of Orders :"))
# with open("Orders.csv","w") as file:
#     writer=csv.writer(file)
#     writer.writerow(["Order Id","Customer","Product","Quantity","Price"])
#     for i in range(Number):
#        print("-"*70)
#        Order_Id=int(input(f"Enter the Order Id of Order {i+1} : "))
#        Customer=str(input("Enter the Customer  :"))
#        Product=str(input("Enter the Product Name  : "))
#        Quantity=int(input("Enter the Quantity  :"))
#        Price=int(input("Enter the Price :"))
#        writer.writerow([Order_Id,Customer,Product,Quantity,Price])
df_csv=pd.read_csv("Orders.csv")
df_csv["Total"] = df_csv["Quantity"] * df_csv["Price"]
df_csv.to_csv("Orders.csv", index=False)
print(df_csv) 
print("-"*70)
print("Highest Order Value :")
print(df_csv[df_csv["Quantity"]==df_csv["Quantity"].max()])
print("-"*70)
print("Lowesr Order Value :")
print(df_csv[df_csv["Quantity"]==df_csv["Quantity"].min()])
print("-"*70)
print("Average Order value  :")
print(df_csv["Quantity"].mean())
print("-"*70)
print(" Order Above 5000  :")
print(df_csv[df_csv[" Total Price"]>5000]) # clear
plt.figure(figsize=(8,6))
plt.subplot(1,2,1)
plt.plot(df_csv["Product"],df_csv["Quantity"],marker="o")
plt.title("Order Value")
plt.grid(True)
plt.subplot(1,2,2)
plt.pie(df_csv["Quantity"],labels=df_csv["Product"],autopct='%1.f%%')
plt.title("Pie Chart → Product Distribution.")
plt.tight_layout()
plt.show()

