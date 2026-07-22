class car:
    def __init__(self,Brand,Model,Price):
        self.Brand=Brand
        self.Model=Model
        self.Price=Price
    def display(self):
        print(f"Car Details\n\tBrand = {self.Brand}\n\tModel = {self.Model}\n\tPrice = {self.Price}")
        print("-"*25)
            
    pass
Car1=car("honda",2021,120000)
Car2=car("Toyata",2020,110000)
Car3=car("Mahindra",2017,140000)
Car1.display()
Car2.display()
Car3.display()