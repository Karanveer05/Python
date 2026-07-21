import numpy as np
import csv
Step=[]
Step_Counts=np.zeros(3,dtype=int)
with open("tracker.csv","w",newline="") as file:
 writer=csv.writer(file)
 writer.writerow(["Day","Steps"])
 for i in range(3):
  Steps=int(input(f"Entered the steps for Day {i+1} :"))
  Step_Counts[i]=Steps
  writer.writerow([f"Day {i+1}",Step_Counts[i]])
print("Data written successfully.")
print("-"*50)
with open("tracker.csv","r",newline="") as file:
 data=csv.reader(file)
 next(data)
 for row in data:
    Step.append(int(row[1]))
print(f"Max steps {max(Step)}")
print("-"*50)
print(f"Min steps {min(Step)}")
print("-"*50)
print(f"Mean steps {sum(Step)/len(Step)}")
print("-"*50)
print(f"Median steps {np.median(Step)}")
print("-"*50)
print(f"Days Having More THan 10,000 Steps are : ")
for i in range(len(Step_Counts)):
    if Step_Counts[i]>10000:
        print(f"Day {i+1}      {Step_Counts} Steps")
