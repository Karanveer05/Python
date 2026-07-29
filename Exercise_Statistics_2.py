import pandas as pd

# Read the CSV file
df = pd.read_csv("mobile_user_data_200.csv")

# create the dictonary with colums and values
statistical_types = {
    "User_ID": "Nominal",
    "screen_Time": "Continuous",
    "Number_of_Apps": "Discrete",
    "Age": "Discrete",
    "Subscription_Type": "Nominal",
    "City": "Nominal"
}
print()
# Create a result DataFrame
result=pd.DataFrame({
    " Data Type":df.dtypes,
    "Type":[
      statistical_types.get(column,"Unknown")
      for column in df.columns
    ]
    
})

print(result)
print("Mean Screen Time is :")
print(df["Screen_Time"].mean())
print("Median Screen_Time is :")
print(df["Screen_Time"].median())
print("  mode of Subscription Type is :")
print(df["Subscription_Type"].mode())
print("Range :")
print(df["Screen_Time"].max()-df["Screen_Time"].min())
print("Variance :")
print(df["Screen_Time"].var())
print("Standard Deviation :")
print(df["Screen_Time"].std())
print(f"Salary Qunatile (Q1) : {df['Screen_Time'].quantile(0.25)}")
print(f"Salary Qunatile (Q2) : {df['Screen_Time'].quantile(0.50)}")
print(f"Salary Qunatile (Q3) : {df['Screen_Time'].quantile(0.75)}")
print("IQR :")
print(df["Screen_Time"].quantile(0.75)-df["Screen_Time"].quantile(0.25))
print(f"User has highest screen time  :")
print(df[df["Screen_Time"]==df["Screen_Time"].max()])