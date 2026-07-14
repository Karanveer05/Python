class BankAccount:
    def __init__(self,Account_Holder,Balance=50000):
        self.Account_Holder=Account_Holder
        self.Balance=Balance
    def deposit(self): 

        amount=int(input("Enter Amount To Be Deposit : "))
        self.Balance=self.Balance+amount
        print(f" Your Balance Is {self.Balance}")
        
    def withdraw(self):
        amount=int(input("Enter Amount To Be Withdraw : "))
        if self.Balance>=amount: 
            self.Balance=self.Balance-amount
            print(f" Your Balance Is {self.Balance}")
        else:
          print(" Your Balance Is Insufficient")
          
    def show_balance(self):
        print(f"your Balance is {self.Balance}")
    pass
Account_Holder1=BankAccount("Karanveer singh")
print("1. Deposit\n2. Withdraw\n3. Balance \n")
select=int(input("Enter the Valid Option :"))
match select:
    case 1:
        Account_Holder1.deposit()
    case 2:
        Account_Holder1.withdraw()
    case 3:
        Account_Holder1.show_balance()
    case _:
        print("Enter Valid Option ")