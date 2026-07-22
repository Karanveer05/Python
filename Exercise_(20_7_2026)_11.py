import numpy as np

Days = np.array(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
Passengers = np.array([10,20,30,40,50,60,70])

print("-"*50)
print(f"Total Passengers : {Passengers.sum()}")

print("-"*50)
print(f"Busiest Day : {Days[Passengers.argmax()]}")

print("-"*50)
print(f"Least Busy Day : {Days[Passengers.argmin()]}")

print("-"*50)
print(f"Average Passengers : {Passengers.mean()}")

print("-"*50)
print("Days with Passengers Above Average :")
print(Days[Passengers > Passengers.mean()])