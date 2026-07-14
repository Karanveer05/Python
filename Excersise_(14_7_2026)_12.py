class Book:
    def __init__(self,Book_Id,Title,Author,Price):
        self.Book_Id=Book_Id
        self.Title=Title
        self.Author=Author
        self.Price=Price
    def display(self):
        print(f"Books Details \n\nBook_Id = {self.Book_Id}\nTitle = {self.Title}\nAuthor = {self.Author}\nPrice = {self.Price} ") 
        print("-"*25)   
    def Find(self):
        ID=int(input("Enter The Book Id : "))
        for Book in Books:
         if Book.Book_Id == ID:
            Book.display() 
            return  
    print("Id Not Found")
    
        
    pass
Book1=Book(1,"Python","x",80)
Book2=Book(2,"c++","y",60)
Book3=Book(3,"Html","z",96)
Book4=Book(4,"Dev","L",70)
Book5=Book(5,"Vs Code","M",80)

Books=[Book1,Book2,Book3,Book4,Book5]
for Book in Books:
 Book.display()
Book.Find()

    