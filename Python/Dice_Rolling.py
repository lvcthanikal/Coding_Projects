#This project is for simulating dice rolls.
#Should be able to roll a dice (d6 or d12)
#Take input from user on whether or not he should reroll.

#Start of the project

#importing the Random file for python
import random



print("Welcome User.")
dice = input("Please select the type of dice you would like: D6 or D12 ")

#check if a dice was chosen
while True:
    if dice.upper() == "D6" or dice.upper() == "D12":
        #exits the while loop
        break
    else:
        #keeps asking for dice until d6 or d12 is choosen
        dice = input("Please choose a proper dice. ")

print("You have selected " + dice.upper() +".")

#checking for right input
while True:
    #Asks user if they would like to roll the dice
    answer = input("Would you like to roll? : Yes/No ")

    if answer.upper() == "YES":
        if dice.upper() == "D6":
            print(random.randint(1,6))
        else:
            print(random.randint(1,12))
    elif answer.upper() == "NO":
        break
    else:
        answer = input("Enter Yes or No: ")
