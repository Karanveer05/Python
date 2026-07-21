import numpy as np
Beds=np.array([True, False, True, False])
print("-"*50)
print(f"The Data type of Array is : {Beds.dtype}")
count=np.count_nonzero(Beds)
print("-"*50)
print(f"The Number of beds Occupied are : {count}")
print("-"*50)
print(f"The Number of beds  Not Occupied are : {Beds.size-count}")
print("-"*50)
print(f"Vacant Beds Displaying By Boolean Indexing : {Beds[Beds==False]}")

