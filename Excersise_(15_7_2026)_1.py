def company_details(**info):
 for key , Value in info.items():
    print(f"{key} = {Value}")
    print("-"*25)
     
company_details(Company_Name="Company_A",Location="Place_A",Employees=20,CEO="person L",Founded_Year=2008)     
# company_details(Company_Name="Company_B",Location="Place_B",Employees=23,CEO="person M",Founded_Year=2005)     
# company_details(Company_Name="Company_C",Location="Place_C",Employees=25,CEO="person N",Founded_Year=2001)     
# company_details(Company_Name="Company_D",Location="Place_D",Employees=28,CEO="person O",Founded_Year=2002)     