# Check voting eligibility
Age = int(input("Enter  Age: "))
Citizenship = input("Enter Citizenship: ")
if Age >= 18 and (Citizenship == "Indian" or Citizenship == "indian" or Citizenship == "INDIAN"):
    print("\tEligible ")
else:
    print("\tNot Eligible")