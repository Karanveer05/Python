def Interest(Principal,time,rate=5):
    return Principal*time*rate
Principal=int(input("Enter the Amount : "))
time=int(input("Enter the in Years : "))
condition=str(input("You want to Define the  of Rate \n Yes\t No\n Enter : "))
if condition.lower() == "yes" :
    rate=int(input("Enter The Rate : "))
    print(f"Interest is {Interest(Principal,time,rate)}")
else :
  print(f"Interest is {Interest(Principal,time)}")

