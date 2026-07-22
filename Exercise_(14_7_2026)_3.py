class Mobile:
    def __init__(self,Brand,Ram,Storage):
        self.Brand=Brand
        self.Ram=Ram
        self.Storage=Storage
    def display(self):
        print(f"Car Details\n\tBrand = {self.Brand}\n\tRam = {self.Ram} GB\n\tStorage = {self.Storage} GB")
        print("-"*25)
            
    pass
mobile1=Mobile("Samsung",8 ,64 )
mobile2=Mobile("Apple",12 ,128 )
mobile3=Mobile("Nokia",16 ,256 )
mobile1.display()
mobile2.display()
mobile3.display()