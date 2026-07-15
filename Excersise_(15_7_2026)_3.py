class Credit_card:
    def pay():
        print("Paid Using Credit Card")
    pass
class UPI:
    def pay():
        print("Paid Using UPI")
    pass
class Cash:
    def pay():
        print("Paid Using Cash")
    pass
pay1=Cash.pay()
pay1=UPI.pay()
pay1=Credit_card.pay()