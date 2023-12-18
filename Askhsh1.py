
#Write a program that generates a random number between 1 and 100. Ask the user to guess the number.
#Provide hints such as "too high" or "too low" after each guess.
# Use a loop to allow the user to keep guessing until they get it right.
# Integrate exception handling to ensure the user inputs a valid number.



import random

x=(random.randint(1,100))


cond = False

while cond != True:
    num1 = input("type an integer number to guess the random number:\n")
    if num1.isdigit():
        num1 = int(num1)

        if num1 > x :
            print("hint:too high")

        elif num1 < x :
            print("hint:too low")
        elif num1 == x:
            cond = True


    else:
        print("error because we want a digit")


print(num1)
print("you found it")