class Employee:
    def __init__(self,Name,ID,Department,Salary):
        self.Employee_Id=ID
        self.Name=Name
        self.Department=Department
        self.Salary=Salary
    def display(self):
        print(f"Employees Details \n\nEmployee_Id = {self.Employee_Id}\nName = {self.Name}\nDepartment = {self.Department}\nSalary= {self.Salary} ") 
        print("-"*25)   
    def Find(self):
        count=0
        print("\n\nEmployee With low salary\n")
        print("-"*25)   
        for Employee in Employees:
         if Employee.Salary <50000:
            count=+1
            Employee.display() 
        if count==0:
            print("No Such Employee Lower Salary Than 50000")   
        return 
    
        
    pass
Employee1=Employee("Karanveer",2315125,"CSE",80000)
Employee2=Employee("Aman",2315124,"It",40000)
Employee3=Employee("Sahil",2315121,"LAW",36000)
Employee4=Employee("Jaskaran",2315122,"B.COM",70000)
Employee5=Employee("Japanpreet",2315120,"Commerce",80000)

Employees=[Employee1,Employee2,Employee3,Employee4,Employee5]
for Employee in Employees:
 Employee.display()
Employee.Find()