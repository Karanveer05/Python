import numpy as np
secret_number = np.random.randint(1, 101)
print(secret_number)

print(" Welcome to the Number Guessing Game!")
print("Guess  between 1 and 100.")
for i in range (4):
    if i<3 :
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
         print("Too low! Try again.")
        elif guess > secret_number:
         print("To High Try again.")
        else:
         print(f"Congratulations! You guessed the number in {i+1} attempts.")
         break
    else:
     print(f"Failed\ncorrect number is : {secret_number}") 
