import pandas as pd

# Read the CSV file
df = pd.read_csv("House.csv")

# create the dictonary with colums and values
statistical_types = {
    "House_ID": "Nominal",
    "City": "Nominal",
    "Area (sq ft)": "Continuous",
    "Bedrooms": "Discrete",
    "Price": "Continuous",
    "Age_of_House": "Discrete"
}
print()
# Create a result DataFrame
result = pd.DataFrame({         
    "Datatype": df.dtypes,                                  
    "Type": [
          statistical_types.get(column, "Unknown")            #syntax   New_Column_Name : Dictonary_Name.get("key_value","Default_Value") 
        for column in df.columns                            #             Loops       # Dictonary_Name.get("key_value","Default_Value")  it returns values
    ]
})

print(result)
print("Mean Price is :")
print(df["Price"].mean())
print("Median Price is :")
print(df["Price"].median())
print(" Price is :")
print(df["Price"].mode())
print("Range :")
print(df["Price"].max()-df["Price"].min())
print("Variance :")
print(df["Price"].var())
print("Standard Deviation :")
print(df["Price"].std())
print(f"Salary Qunatile (Q1) : {df['Price'].quantile(0.25)}")
print(f"Salary Qunatile (Q2) : {df['Price'].quantile(0.50)}")
print(f"Salary Qunatile (Q3) : {df['Price'].quantile(0.75)}")
print("IQR :")
print(df["Price"].quantile(0.75)-df["Price"].quantile(0.25))
#median in better because it tell us the median values as it give us the mid values