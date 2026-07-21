import numpy as np

print("Enter the Runs Scored by Batsmen")
print("-" * 35)

Array_Runs = np.empty(10, dtype=int)  # reserves empty arry with 10 reserved places of int data type

for i in range(10):
    Array_Runs[i] = int(input(f"Enter Run Scored By Batsman {i+1}: "))

print("-" * 35)
print("Displaying the Scores of Batsmen")
print(Array_Runs)