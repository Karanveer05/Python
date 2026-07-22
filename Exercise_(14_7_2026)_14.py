class Product:
    def __init__(self,Product_Name,ID,Quantity,Price):
        self.Product_Name=Product_Name
        self.ID=ID
        self.Quantity=Quantity
        self.Price=Price
    def display(self):
        print(f"Products Details : \n \nProduct_Name = {self.Product_Name}\nID = {self.ID}\nQuantity = {self.Quantity}\nPrice = {self.Price} ")    
    def Stock_value(self):
        Stock_Value=Product.Quantity*Product.Price
        print("The Stock Value Is ",Stock_Value)
        print("-"*25)
    pass
Product1=Product("A",1,20,800)
Product2=Product("B",2,12,600)
Product3=Product("C",3,14,960)
Product4=Product("C",4,16,700)
Product5=Product("D",5,22,800)

Products=[Product1,Product2,Product3,Product4,Product5]
for Product in Products :
    Product.display()
    Product.Stock_value()
