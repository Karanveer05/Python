#Check pass or fail.
Maths = float(input("Enter your marks in Maths: "))
Science = float(input("Enter your marks in Science: "))
Computer = float(input("Enter your marks in Computer: "))
Percentage = (Maths + Science + Computer) / 3*100
if Percentage >= 40:
    print("You have passed.")
else:
    print("You have failed.")