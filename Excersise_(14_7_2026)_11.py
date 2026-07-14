class Student:
    def __init__(self,Name,Roll_no,Course,Marks):
        self.Name=Name
        self.Roll_no=Roll_no
        self.Course=Course
        self.Marks=Marks
    def display(self):
        print(f"Students Details \nName = {self.Name}\nRoll_No = {self.Roll_no}\nCourse = {self.Course}\nMarks = {self.Marks} ") 
        print("-"*25)   
        
    pass
Student1=Student("Karanveer",2315125,"CSE",80)
Student2=Student("Aman",2315124,"It",60)
Student3=Student("Sahil",2315121,"LAW",96)
Student4=Student("Jaskaran",2315122,"B.COM",70)
Student5=Student("Japanpreet",2315120,"Commerce",80)

Students=[Student1,Student2,Student3,Student4,Student5]
for Student in Students :
    Student.display()
    