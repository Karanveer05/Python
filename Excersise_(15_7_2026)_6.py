# import csv

# with open("Student.csv", "w", newline="") as file:
#    writer = csv.writer(file)
 
#    writer.writerow(["Product ID","Product Name","Price","Quantity"])
 
#    Number=int(input("Enter the Number of Products you Want to enter : "))
 
# for i in range (Number):
#     print(f"Enter details for Product : {i+1}\n")
#     Product_ID=int(input("Enter The Product Id : "))
#     Product_Name=str(input("Enter The Product Name : "))
#     Price=int(input("Enter The Product Price : "))
#     Quantity=int(input("Enter The Product Quantity : "))
#     with open("Student.csv", "a", newline="") as file:
#      writer = csv.writer(file)
#      writer.writerow([Product_ID,Product_Name,Price,Quantity])
#     print("-"*25)
    
# print("\nData Entered to file is successful")    

import csv

file=open("Student.csv","a")
 
file.write("Product ID,Product Name,Price,Quantity\n")
 
Number=int(input("Enter the Number of Products you Want to enter : "))
 
for i in range (Number):
    print(f"Enter details for Product : {i+1}\n")
    Product_ID=int(input("Enter The Product Id : "))
    Product_Name=str(input("Enter The Product Name : "))
    Price=int(input("Enter The Product Price : "))
    Quantity=int(input("Enter The Product Quantity : "))
    file.write(f"{Product_ID},{Product_Name},{Price},{Quantity}\n")
    print("-"*25)
    
print("\nData Entered to file is successful")    