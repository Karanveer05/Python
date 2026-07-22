#Write lambda functions to perform the following operations:
# Find the square of a number.
# Find the larger of two numbers
Square=lambda number :number*number
largest_number=lambda a,b : a if a>b else b
number=int(input("Enter the Number For Square :"))
a=int(input("Enter the 1st Number : "))
b=int(input("Enter the 2nd Number : "))
print(f"The Square is {Square(number)}")
print(f"The Largest is {largest_number(a,b)}")