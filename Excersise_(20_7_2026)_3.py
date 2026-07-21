import pandas as pd
Planets=pd.Series([100 ,200,300,400,500],index=["Mercury","Venus","Earth","Mars","Jupiter"])
print("-"*50)
print("Displaying the Information of Planets ")
for planets , distance in Planets.items():
    print(f"{planets}  :  {distance} Million KM")
print("-"*50)
print(f"The Distance of Earth in KM  :{ Planets['Earth']} Million KM")
print("-"*50)
for planets , distance in Planets[:3].items():
    print(f"{planets}  :  {distance} Million KM")
print("-"*50)
