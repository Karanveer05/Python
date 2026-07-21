
File=open("water_log.txt","w") 
print("-"*50)
File.write(" Detail of Store the daily water intake (in liters) for 7 days\n")
for i  in range(7):
    Amount_of_Water=int(input(f"Enter the Water Amount Stores on {i+1} day :"))
    File.write(f" Day {i+1}  : {Amount_of_Water} \n")
File.close()
print("-"*50)
print("Reading The File :")
File=open("water_log.txt","r") 
print(File.read())

    