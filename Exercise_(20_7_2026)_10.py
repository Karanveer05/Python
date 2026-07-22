import csv
import numpy as np
Units=[]
with open ("electricity.csv","w",newline="") as file:
 writer=csv.writer(file)
 writer.writerow(["House Number","Units consumed"])
 Number=int(input("Enter the Number of Houses : "))
 print("-"*60)
 for i in range(Number):
    House_Number=int(input("Enter the House Number :"))
    Units_consumed=int(input("Enter the Units consumed :"))
    Units.append(Units_consumed)
    writer.writerow([House_Number,Units_consumed])
print("Data Export to file Sucessfull")   
print("-"*60)
with open ("electricity.csv","r") as file: 
 data=csv.reader(file)
 next(data)
 for row in data:
    print(f"The House Number is : {row[0]}    The Units Consumed is {row[1]} KWh")
print("-"*60)
print(f"Total units are  :{sum(Units)}")
print("-"*60)
print(f"Average units are  :{sum(Units)/len(Units)}")
print("-"*60)
print(f"Max units are  : {max(Units)}\n House No : {row [row[1]==min(Units)]}")
print("-"*60)
print(f"Min units are  : {min(Units)}\n House no :{row[row[1]==min(Units)]}")
