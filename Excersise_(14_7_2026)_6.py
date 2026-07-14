class Student:
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks
        
    def display(self):
        print(f"Student Details\n\tName = {self.Name}\n\tMarks = {self.Marks} ")
        
    def result(self):
        if self.Marks>=40:
             print("\tPass")
        else :
          print("\tFail")
        print("-"*25)
        
            
    pass
Student1=Student("Ram",64 )
Student2=Student("Mohan ",25 )
Student3=Student("Aman",67 )
Student1.display()
Student1.result()
Student2.display()
Student1.result()
Student3.display()
Student1.result()