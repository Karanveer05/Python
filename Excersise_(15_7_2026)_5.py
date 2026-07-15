file=open("attendence.txt","a")
Number=int(input("Enter the  NO of Students names you want to enter in the list :"))
for i in range(0,Number):
 Name=str(input(f"Enter the Name of Student {i+1} : "))
 file.write(f"Name of Student {i+1} : {Name}\n")
file.close()
