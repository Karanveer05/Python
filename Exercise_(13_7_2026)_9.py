counter=0
def Increment():
    global counter
    counter+=1


for i in range(5):
 Increment()

 print(f"The value of Global Variable Is {counter}")