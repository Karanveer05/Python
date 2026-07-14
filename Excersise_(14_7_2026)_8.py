class Rectangle:
    def __init__(self,Length,Width):
        self.Length=Length
        self.Width=Width
    def display_Perimeter(self):
        print(f"Rectangle Area  Details\n\tLength = {self.Length}\n\tParimeter is ",2*self.Length*self.Width)
        print("-"*25)
    def display_area(self):
        print(f"Rectangle  Perimeter Details\n\tLength = {self.Length}\n\t = {self.Width}\n\t Area is ",self.Length*self.Width)
        print("-"*25)
            
    pass
Rectangle1=Rectangle(10,20)
Rectangle1.display_area()
Rectangle1.display_Perimeter()