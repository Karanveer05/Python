import pandas as pd
import matplotlib.pyplot as plt
data ={
 "Name":['A','B','C'],
 "Course":["x","Y","Z"],
 "Percentage":[80,94,45],
 "City":["Delhi","Bc","Cd"]
}
df=pd.DataFrame(data)
df.to_csv("Student_Report.csv")
print(df)
print("Percentage Above 80 ")
print(df[df["Percentage"]>80])
print("Student from delhi ")
print(df[df["City"].str.upper()=="DELHI"])
print("Average Percentage :")
print(df["Percentage"].mean())
print("No of student per course :")
print(df["Course"].value_counts())
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.bar(df["Name"],df["Percentage"])
plt.ylabel("Percentage")
plt.xlabel("Name")
plt.title("Bar Chart → Student Percentage.")
plt.grid(True)
plt.subplot(1,2,2)
plt.pie(df["Course"].value_counts(),labels=df["Course"],autopct='%1.f%%')
plt.title(" Pie Chart → Course Distribution.")
plt.tight_layout()
plt.show()
