import csv
class paitent:
    Number=0 
    def Inputs():
        Number=int(input("Enter The Number Of Patients : \n"))
        for i in range (0,Number):
         print("-"*25)
         print(f"Enter the Detail of {i+1} Paitent \n")
         Name=str(input("Enter the Name : "))
         Patient_Id=int(input("Enter the ID : "))
         Disease=str(input("Enter the Disease : "))
         Age=str(input("Enter the Age : "))
         file.write(f"{Name},{Patient_Id},{Disease},{Age}\n")
    def Outputs():
     with open("Patient_Data.csv", "r") as file:
       data = csv.reader(file)
       next(data)
       for row in data:
           print("-"*25)
           print(f"Name \t : {row[0]}\nPatient ID : {row[1]}\nDisease : {row[2]}\nAge \t: {row[3]}")
          
    pass
file=open("Patient_Data.csv","w")
file.write("Patient Name,Patient_Id,Disease,Age\n")
Patients=paitent.Inputs()
file.close()
Patients=paitent.Outputs()