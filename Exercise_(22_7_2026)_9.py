import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Order ID": [1, 2, 3],
    "Food Item": ["Pizza", "Burger", "Pasta"],
    "Quantity": [2, 4, 3],
    "Price": [250, 150, 200],
    "Payment Mode": ["Online", "Offline", "Online"]
}

df = pd.DataFrame(data)

df["Total"] = df["Quantity"] * df["Price"]

df.to_csv("Restaurant.csv", index=False)

print(df)

print("-" * 50)
print("Total Revenue:")
print(df["Total"].sum())

print("-" * 50)
print("Most Ordered Item:")
print(df[df["Quantity"] == df["Quantity"].max()])

print("-" * 50)
print("Highest Bill:")
print(df[df["Total"] == df["Total"].max()])

print("-" * 50)
print("Lowest Bill:")
print(df[df["Total"] == df["Total"].min()])

print("-" * 50)
print("Average Bill:")
print(df["Total"].mean())

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
payment_count = df["Payment Mode"].value_counts()
plt.pie(payment_count,
        labels=payment_count.index,
        autopct="%1.1f%%")
plt.title("Payment Mode")

plt.subplot(2, 2, 2)
plt.bar(df["Food Item"], df["Total"])
plt.xlabel("Food Item")
plt.ylabel("Sales")
plt.title("Food Sales")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.hist(df["Total"], bins="auto")
plt.xlabel("Bill Amount")
plt.ylabel("Frequency")
plt.title("Bill Distribution")

plt.tight_layout()
plt.show()