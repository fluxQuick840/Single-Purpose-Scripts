#Rock, Paper, Scissors! A delightful game gone virtual
from random import randint
from time import sleep

#defining variables for rock, paper, scissors to reduce the size of print statements
rock = chr(9994)
paper = chr(9995)
scissors = chr(9996)

#A welcome message
input("Hello, and welcome to Rock Paper Scissors!\nBefore we get started, let's make sure you know how to play.\nPress enter to continue.")
#setting a variable to control the instruction loop and initializing that
breaker = 1
while breaker == 1:
#display instructions
    print("Ok. So to start, you'll be playing this game against the computer.\n")
    sleep(1)
    print("in this game, you will choose either rock, paper or scissors, and the computer will do the same\n")
    sleep(1)
    print(f"Rock: {rock} breaks Scissors: {scissors}")
    sleep(1)
    print(f"Paper: {paper} covers rock: {rock}")
    sleep(1)
    print(f"Scissors: {scissors} cuts paper: {paper}")
    sleep(1)
    print("To choose an option, you'll type:\n1, for rock\n2, for paper, and\n3, for scissors.\n")
    sleep(1)
    print("You good?\n")
#making sure the user understands, initializing another loop for input validation
    while True:
        answer = input("Type y if you got that, or n if you would like to read those instructions again:\n")
        if answer == 'y': #if they got that
            breaker = 0 #setting our loop control variable to 0 to break the outer loop
            break #breaking this loop
        elif answer == 'n': #If they need to read that again
            print("Here they are again")
            break
        else: #The user didn't type the input we were looking for
            print("please type y or n")

#defining a function to check for the winner of each round
def win(computer_choice,user_choice):
    if computer_choice == user_choice:
        winner = "You Tied!"
#programming conditionals for every situation where the user could win
    elif computer_choice == 1 and user_choice == 2:
        winner = "You Won!"
    elif computer_choice == 2 and user_choice == 3:
        winner = "You Won!"
    elif computer_choice == 3 and user_choice == 1:
        winner = "You Won!"
    else: #if any other situation, the user lost
        winner = "You Lost."
    return winner

#defining our main play function
def play():
#initializing another input validation loop
    while True:
        print("rock",rock,"Paper",paper,"scissors",scissors)
        user_choice = input("shoot!")
        if (user_choice.isdigit()): #if user_choice is a number
            user_choice = int(user_choice) #type cast to int for value comparison
            if user_choice > 3: #there are only three options, 
                print("please enter 1, 2, or 3")
            else: #No problems
                break
        else: #user_choice was not an number
            print("please type 1, 2, or 3")
#randomly generating a value for the computer
    computer_choice = randint(1,3)
#checking to see who won and assigning that to our result variable
    result = win(computer_choice,user_choice)
#defining a dictionary so we can print out user friendly results instead of numbers
    translation = {
      1 : "Rock",
      2 : "Paper",
      3 : "scissors"
    }
#looping through the dictionary for user_choice
    for i in translation:
        if i == user_choice: #if i matches one of the dictionary keys
            user_choice = translation.get(i) #assign that value to user_choice instead of the original number the user input
#same drill for computer_choice
    for i in translation:
        if i == computer_choice:
            computer_choice = translation.get(i)
#display results
    print("you chose",user_choice)
    print("the computer chose",computer_choice)
    print(result)
#initializing another validation loop to check input for users choice to play again or not
    while True:
        again = input("Do you want to play again? Type y for yes or n for no")
        if again == 'y':
            print("OK!")
            break
        if again == 'n':
            print("Ok, bye.")
            exit() #quit the program
        else:
            print("Please type y or n")

#initializing the main program loop
while True:
#calling our play function, which will be called again until the user exits
    play()
