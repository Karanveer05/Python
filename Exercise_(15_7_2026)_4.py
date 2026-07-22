class SmartTV:
 _volume=20
 def increase_volume():
     input_value=int(input("Enter the Number bY Volume Increased : "))
     if(input_value+SmartTV._volume<100):
         input_value=input_value+SmartTV._volume
         print(f"Volume Now is : {input_value}\n")
     else:
         print("Invalid Input")
    

 def decrease_volume():
     input_value=int(input("Enter the Number bY Volume decreased :"))
     if(input_value-SmartTV._volume<0):
         input_value=SmartTV._volume-input_value
         print(f"Volume Now is : {input_value}\n")
     else:
         print("Invalid Input")

 def show_volume():
        print(f"The current volume is : {SmartTV._volume}")   
          
pass

input1=SmartTV.increase_volume()
input2=SmartTV.decrease_volume()
input3=SmartTV.show_volume()