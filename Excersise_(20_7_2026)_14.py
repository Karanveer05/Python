import numpy as np

Temp = np.random.randint(20, 41, 15)
print(Temp)

print("-"*50)
print(f"Days above 35°C : {np.count_nonzero(Temp>35)}")

print("-"*50)
print(f"Days below 20°C : {np.count_nonzero(Temp < 20)}")

print("-"*50)
print(f"Temperatures between 25°C and 30°C : {np.count_nonzero((Temp >= 25) & (Temp <= 30))}")

