class Student:
    def __init__(self,Name,Roll_no,Course,Marks):
        self.Name=Name
        self.Roll_no=Roll_no
        self.Course=Course
        self.Marks=Marks
    def display(self):
        print(f"Students Details \nName = {self.Name}\nRoll_No = {self.Roll_no}\nCourse = {self.Course}\nMarks = {self.Marks} ")   
    def Grade(self):
        if self.Marks>=90:
            print("The Grade is A")
        elif self.Marks>=75:
            print("The Grade is B")
        elif self.Marks>=50:
            print("The Grade is C")
        else:
            print("Fail")
        print("-"*25) 
    def Highest_Marks(self):
        Maximum=0
        ID_Record=0
        for Student in Students:
            if Maximum <= Student.Marks:
                Maximum=Student.Marks 
        print("The Maximum Marks Of the Student is ",Maximum) 
    def Average(self):
        Total=0
        for Student in Students:
         Total = Total + Student.Marks
        print("The Average Marks Of The Students Is ",Total/5,"\n")
        
          
        
    pass
Student1=Student("Karanveer",2315125,"CSE",90)
Student2=Student("Aman",2315124,"It",60)
Student3=Student("Sahil",2315121,"LAW",56)
Student4=Student("Jaskaran",2315122,"B.COM",70)
Student5=Student("Japanpreet",2315120,"Commerce",20)

Students=[Student1,Student2,Student3,Student4,Student5]
for Student in Students :
    Student.display()
    Student.Grade()
    
Student.Average()
Student.Highest_Marks()
    
    
