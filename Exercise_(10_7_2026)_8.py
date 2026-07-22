# ATM PIN verification
Account_Number = int(input("Enter your account number: "))
Pin=int(input("Enter your PIN: "))
if Account_Number == 12345 :
    if Pin == 1234:
        print("Access granted. Welcome!")
    else:
        print("Incorrect PIN")
else:
    print("Wrong Account Number")
