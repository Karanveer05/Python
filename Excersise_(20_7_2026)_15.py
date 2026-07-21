import csv
with open("Olympic_medal.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["COUNTRY","GOLD","SILVER","BRONZE"])
    Number=int(input("Enter the number of Countries you want to add on data :"))
    for i in range(Number):
     Name=str(input(f"Enter The Name of the country {i+1} :"))
     Gold=str(input(f"Enter The Gold Medal by {Name} :"))
     Silver=str(input(f"Enter The Silver Medal by {Name} :"))
     Bronze=str(input(f"Enter The Bronze Medal by {Name} :"))
     writer.writerow([Name,Gold,Silver,Bronze])
print("Export the data to file is sucessfull")
with open("Olympic_medal.csv","r")as file:
    data=csv.reader(file)
    next(data)
    for row in data:
      print("-"*50)
      print(f"Country : {row[0]}\nGold : {row[1]}\nSilver : {row[2]}\nBronze : {row[3]}\n")
   