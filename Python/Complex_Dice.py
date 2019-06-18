#this is for rolling anyset of dice that is choosen by the user

import random


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
        dice = dice.upper()
        #taking the int value for the string that was entered
        number = dice.split("D")
        #checking the length of the array
        if len(number) == 1:
            #result
            print(random.randint(1,int(number[0])))
        else:
            #result
            print(random.randint(1,int(number[1])))
    #if no proper answer was given to the question
    else:
        print("Please enter a proper response!")
