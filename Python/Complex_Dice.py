#this is for rolling anyset of dice that is choosen by the user

import random
import re

print("Welcome to the first project.")
print("This is for rolling any type of dice that you want.")

#looping the choice of whether or not a person wants to roll the dice.
while True:
    answer = input("Do you want to roll a dice: Yes/No ")

    #if the user says no
    if answer.upper() == "NO":
        break
    #if the user says yes
    elif answer.upper() == "YES":
        print("Good choice!")

        #taking the input for the number of sides the dice has
        dice = input("Select the number of sides on the dice: ")
        #taking the int value for the string that was entered
        while True:
            if dice.isdigit():
                number = int(re.search(r'\d+', dice).group())
                #result
                print(random.randint(1,number))
                break
            else:
                dice = input("Please enter a number! ")

    #if no proper answer was given to the question
    else:
        print("Please enter a proper response!")
