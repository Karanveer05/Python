import numpy as np
Air_Quality=np.random.randint(1,150,30)
print("-"*50)
print(Air_Quality)
print("-"*50)
print(f"Good Air Quality : {np.count_nonzero(Air_Quality<50)} Days")
print("-"*50)
print(f"Moderate Air Quality : {np.count_nonzero((Air_Quality >= 50) & (Air_Quality <= 100))} Days")
print("-"*50)
print(f"Poor Air Quality : {np.count_nonzero(Air_Quality>100)} Days")
print("-"*50)

