
class BOOK:
    def __init__(self,Title,Author,Price):
        self.Title=Title
        self.Author=Author
        self.Price=Price
    def display(self):
        print(f"Book Details\n\tBOOK Title = {self.Title}\n\tAuthor = {self.Author} \n\tPrice = {self.Price} ")
        print("-"*25)
            
    pass
BOOK1=BOOK("Life","abc",1200 )

BOOK1.display()
