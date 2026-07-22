import numpy as np
import pandas as pd
Price_=np.zeros(30,dtype=int)
for i in range(30):
    Price=int(input(f"Enter the price for {i+1} Room  : "))
    Price_[i]=Price
New_Price=Price_.reshape(5,6)
print("-"*50)
print("Displaying the matrix")
print(New_Price)
print("-"*50)
print(f"Most Expensive Room is {np.where(New_Price==New_Price.max())}")
print("-"*50)
print(f"Most Chepest  Room is {np.where(New_Price==New_Price.min())}")
print("-"*50)
print(f"Revenue Per Floor is {New_Price.sum(axis=1)}")
print("-"*50)
print(f"Revenue Per Room Type is {New_Price.sum(axis=0)}")
