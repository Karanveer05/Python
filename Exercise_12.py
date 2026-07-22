Customer_Name=input("Enter Customer Name :")
Food_Item_1_Price=int(input("Enter Food Item 1 Price :"))
Food_Item_2_Price=int(input("Enter Food Item 2 Price :"))
Food_Item_3_Price=int(input("Enter Food Item 3 Price :"))
GST_Percentage=int(input("Enter GST Percentage :"))
Total_Food_Bill=Food_Item_1_Price+Food_Item_2_Price+Food_Item_3_Price
GST_Amount=(Total_Food_Bill*GST_Percentage)/100
Final_Bill=Total_Food_Bill+GST_Amount
print("\nCustomer Name : ",Customer_Name)
print("\nFood Total    : ₹",Total_Food_Bill)
print("GST (",GST_Percentage,"%)   : ₹",GST_Amount)
print("----------------------------------")
print("Final Bill    : ₹",Final_Bill)