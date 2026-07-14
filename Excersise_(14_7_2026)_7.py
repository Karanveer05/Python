class Employee:
    def __init__(self,Name,Salary):
        self.Name=Name
        self.Salary=Salary
        
    def display(self):
        print(f"Employee Details\n\tName = {self.Name}\n\tSalary = {self.Salary} ")
        
    def BONUS(self):
        Bonus=(self.Salary)*10/100
        if self.Salary>=50000:
             print("Bonus Ammount : ",Bonus*2)
        else :
             print("Bonus Ammount : ",Bonus)
        print("-"*25)
        
            
    pass
Employee1=Employee("Ram",64000 )
Employee2=Employee("Mohan ",25000 )
Employee3=Employee("Aman",67000 )
Employee1.display()
Employee1.BONUS()
Employee2.display()
Employee2.BONUS()
Employee3.display()
Employee3.BONUS()