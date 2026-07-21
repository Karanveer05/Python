import csv
import numpy as np
Petrol=[]
Diesel=[]
# with open("Fuel_Station_Sales_Report.csv","w",newline="") as file :
#     writer=csv.writer(file)
#     writer.writerow(["Date","Petrol Sold","Diesel Sold"])
#     Number_of_Days=int(input("Enter the Number of Days You Want to enter the date in it :"))
#     for i in range(Number_of_Days):
#         Date=int(input("Enter the Date (DD-MM-YYYY)  :"))
#         Petrol_Sold=int(input("Petrol Sold In ltr.   :"))
#         Diesel_Sold=int(input("Diesel Sold in ltr.   :"))
#         writer.writerow([Date,Petrol_Sold,Diesel_Sold])
# print("Data Exported to file Sucessfull")
with open("Fuel_Station_Sales_Report.csv","r")as file:
    data=csv.reader(file)
    next(data)
    for row in data:
      print("-"*50)
      print(f"Date : {row[0][:2]}/{row[0][2:4]}/{row[0][4:]} \nPetrol Sold: {row[1]}\nDiesel Sold : {row[2]}\n") #row[index][str_start:str_end]
      Petrol.append(int(row[1]))
      Diesel.append(int(row[2]))
print("-"*50)
print(f"Total Petrol Sold :{max(Petrol)}")
print("-"*50)
print(f"Total Diesel Sold :{max(Diesel)}")
print("-"*50)
print(f"Average Petrol Sales :{np.mean(Petrol)}")
print("-"*50)
print(f"Average Diesel Sales :{np.mean(Diesel)}")
print("-"*50)
print(Petrol.index(max(Petrol)))
print(f"Highest Petrol Sales :{Petrol.index(max(Petrol))}")
print("-"*50)
print(f"Highest Diesel Sales :{Diesel.index(max(Diesel))}")
