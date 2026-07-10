#Check pass or fail.
Maths = float(input("Enter your marks in Maths Out of 100 : "))
Science = float(input("Enter your marks in Science Out of 100 : "))
Computer = float(input("Enter your marks in Computer Out of 100 : "))
Percentage = (Maths + Science + Computer) / 3
if Percentage >= 40:
    print("You have passed.")
else:
    print("You have failed.")