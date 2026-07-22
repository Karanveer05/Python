# Find the largest of three numbers.
Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))
Number3 = float(input("Enter third number: "))
if Number1 >=Number2 and Number1 >= Number3:
    print("Largest number is:", Number1)
elif Number2 >= Number1 and Number2 >= Number3:
    print("Largest number is:", Number2)
else:
    print("Largest number is:", Number3)