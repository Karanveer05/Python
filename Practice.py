class employee:
 def __init__(self):
     print("Constructor called succesfully")
 def sum(self,*num):
     print(sum(num))
pass
object = employee()
object.sum(1,22,34,3)