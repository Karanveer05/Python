import pandas as pd
import matplotlib.pyplot as plt
data ={
 "Name":['A','B','C'],
 "Age":[21,23,56],
 "Weight":[200,24,75],
 "Plan":[1,1,1],
 "Fee":[2000,100,1500],
}
df=pd.DataFrame(data)
print(df)
print("Members above 30 years")
print(df[df["Age"]>30])
print("Premimum members")
print(df[df["Plan"]==1])
print("Average fee :")
print(df["Fee"].mean())
print("Max fee :")
print(df["Fee"].max())
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.bar(df["Name"],df["Fee"])
plt.ylabel("Fee")
plt.xlabel("Name")
plt.title(" Bar Chart → Monthly Fee.")
plt.grid(True)
plt.subplot(2,2,2)
plt.scatter(df["Age"],df["Weight"])
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title(" Scatter Plot → Age vs Weight.")
plt.grid(True)
plt.subplot(2,2,3)
plt.pie(df["Plan"],labels=df["Name"],autopct='%1.f%%')
plt.title(" Pie Chart → Membership Plan.")
plt.tight_layout()
plt.show()
