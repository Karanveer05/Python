import pandas as pd
import matplotlib.pyplot as plt
data ={
 "City":['A','B','C'],
 "Temperature":[23,34,45],
 "Humidity":[200,50,70],
 "Rainfall":[3,4,5],
}
df=pd.DataFrame(data)
print(df)
print("Temp Greater than 35 degree :")
print(df[df["Temperature"]>35])
print("Humidity Greater than  70 :")
print(df[df["Humidity"]>70])
print("Average rainfall:")
print(df["Rainfall"].mean())
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.scatter(df["Temperature"],df["Humidity"])
plt.xlabel("Temprature")
plt.ylabel("Humidity")
plt.title(" Scatter Plot → Temperature vs Humidity.")
plt.grid(True)
plt.subplot(2,2,2)
plt.hist(df["Temperature"],bins="auto")
plt.ylabel("Temprature")
plt.title(" Histogram → Temperature.")
plt.grid(True)
plt.subplot(2,2,3)
plt.plot(df["Rainfall"],marker="o")
plt.ylabel("Rainfall")
plt.title(" Line Plot → Rainfall.")
plt.grid(True)
plt.tight_layout()
plt.show()
