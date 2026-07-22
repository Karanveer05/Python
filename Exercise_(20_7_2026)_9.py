import pandas as pd
Course=pd.Series([9,3,8,6,9,5,8.6,9.4,3,9.5],index=["course_1","course_2","course_3","course_4","course_5","course_6","course_7","course_8","course_9","course_10"])
print("-"*50)
print(f"Maximum Rating: of {Course[Course==Course.max()]} = {Course.max()}")
print("-"*50)
print(f"Minimum Rating: of {Course[Course==Course.min()]} = {Course.min()}")      # not read '= 'asigning operator as print statement
print("-"*50)
print(f"Average Rating: {Course.mean()}")
print("-"*50)
print(f"Course With Rating Greater Then 4 are :\n{Course[Course>4]}")  