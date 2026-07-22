class Laptop:
    def __init__(self,Processor,Brand,Ram,Price):
        self.Brand=Brand
        self.Ram=Ram
        self.Price=Price
        self.Processor=Processor
    def display(self):
        print(f"Laptop Details\n\tBrand = {self.Brand}\n\tRam = {self.Ram} GB\n\tPrice = ${self.Price}\n\tProcessor = {self.Processor} ")
        print("-"*25)
            
    pass
Laptop1=Laptop("i5","Samsung",8 ,64000 )
Laptop2=Laptop("MAc i20","MAC",12 ,128000 )
Laptop3=Laptop("i7","Lenovo",16 ,25600 )
Laptop1.display()
Laptop2.display()
Laptop3.display()