import numpy as np
import pandas as pd
print("Enter the Detalus of Mobile Phones")
list_of_phones={}
for i in range(3):
    Name=str(input(f"Enter The Name of {i+1} SmartPhone : "))
    Price=int(input(f"Enter The Price of {i+1} SmartPhone : "))
    list_of_phones[Name]=Price
Mobile_Phone_array= pd.Series(list_of_phones)    ## here coverteed into series
print("-"*50)
print("The Details  of Phones are :")
for name, price in Mobile_Phone_array.items():
    print(f"{name} : ${price}")
print("-"*50)
print(f"The Chepest Phone Is : {np.min(Mobile_Phone_array)}")
print("-"*50)
print(f"The Average Price of  Phone Is : {np.mean(Mobile_Phone_array)}")
print("-"*50)
print(f"The Standard Devation of  Phone Is : {np.std(Mobile_Phone_array)}")
print("-"*50)
print(f"The Phone Cost More than 30,000 are :\n {Mobile_Phone_array[Mobile_Phone_array>30000]}")
