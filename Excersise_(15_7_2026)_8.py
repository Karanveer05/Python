import csv
class Movie:
    Number=0 
    def Inputs():
        Number=int(input("Enter The Number Of Movies : \n"))
        for i in range (0,Number):
         print("-"*25)
         print(f"Enter the Detail of {i+1} Movie \n")
         Movie_Name=str(input("Enter the Movie_Name : "))
         Movie_Id=int(input("Enter the ID : "))
         Rating=int(input("Enter the Rating out of 10 : "))
         if Rating >=10:
              print("Invalid Rating")
              break
         Language=str(input("Enter the Language : "))
         file.write(f"{Movie_Name},{Movie_Id},{Rating},{Language}\n")
    def Outputs():
     with open("Movie_Data.csv", "r") as file:
       data = csv.reader(file)
       next(data)
       for row in data:
           print("-"*25)
           print(f"Movie Name : {row[0]}\nMovie ID : {row[1]}\nRating : {row[2]}\nLanguage : {row[3]}  -- {Movie.is_hit(int(row[2]))} ")
    def is_hit(Rating):
        if Rating>=8:
            return "Hit Movie"
        else: 
            return "Average Movie"
    pass
file=open("Movie_Data.csv","w")
file.write("Movie_Name,Movie_Id,Rating,Language\n")
Patients=Movie.Inputs()
file.close()
Patients=Movie.Outputs()