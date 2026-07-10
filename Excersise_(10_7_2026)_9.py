#Login system
Admin_id = int(input("Enter your Admin Id : "))
Passcode=int(input("Enter your Passcode: "))
if Admin_id == 12345 :
    if Passcode == 1234:
        print("Access granted. Welcome!")
    else:
        print("Incorrect Passcode")
else:
    print("Wrong Admin Id")