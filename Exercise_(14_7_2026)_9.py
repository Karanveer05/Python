class Circle:
    def __init__(self,Radius):
        self.Radius=Radius
    def display_Perimeter(self):
        print(f"Circle Perimeter  Details\n\tParimeter is ",2*self.Radius*3.14)
        print("-"*25)
    def display_area(self):
        print(f"Circle  Area Details\n\t Area is ",self.Radius*self.Radius*3.14)
        print("-"*25)
            
    pass
circle1=Circle(10)
circle1.display_area()
circle1.display_Perimeter()