Employee_Name=input("Enter Employee Name :")
Basic_Salary=float(input("Enter Basic Salary :"))
HRA=float(input("Enter HRA :"))
Bonus=float(input("Enter Bonus :"))
Tax_Deduction=float(input("Enter Tax Deduction :"))
Gross_Salary = Basic_Salary + HRA + Bonus
Net_Salary = Gross_Salary - Tax_Deduction
print("\n==================================")
print("          SALARY SLIP")
print("==================================")
print("Employee Name : ", Employee_Name,"\nBasic Salary  : ₹", Basic_Salary,"\nHRA           : ₹", HRA,"\nBonus         : ₹", Bonus,"\nTax Deduction : ₹", Tax_Deduction)
print("\n----------------------------------\n")
print("Gross Salary  : ₹", Gross_Salary,"\nNet Salary    : ₹", Net_Salary)
print("==================================")
