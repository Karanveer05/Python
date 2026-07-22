def Details(**Info):
    print(Info)

Number_of_Details=int(input("Enter The Number of Of Details You Want TO fill  1-3: "))
match Number_of_Details:
    case 1:
        Name=str(input("Enter the Name :"))
        Details(Name=Name)
    case 2:
        Name=str(input("Enter the Name : "))
        Department=str(input("Enter the Department : "))
        Details(Name=Name,Department=Department)
    case 3:
        Name=str(input("Enter the Name : "))
        Department=str(input("Enter the Department : "))
        salary=int(input("Enter the salary : "))
        Details(Name=Name,Department=Department,Salary=salary)
    case _:
        print("Enter the valid Number!!!")


