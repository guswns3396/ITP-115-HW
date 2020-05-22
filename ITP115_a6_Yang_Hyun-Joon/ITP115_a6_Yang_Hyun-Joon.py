# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 6
# yanghyun@usc.edu

# import necessary module
import random

def main():
    # initialize variables
    playAgain = True
    userChoice = ""
    pcChoice = ""
    result = 0
    # list variable to store scores (index 0 => pc win, index 1 => ties, index 2 => player win)
    score = [0, 0, 0]

    print("\nWelcome! Let's play rock, paper, scissors.")

    while playAgain:

        # print rules
        displayMenu()
        # get userChoice
        userChoice = getPlayerChoice()
        # get pcChoice
        pcChoice = getComputerChoice()
        # determine result
        result = playRound(pcChoice, userChoice)

        # update score
        # if pc wins, update pc score
        if result == -1:
            print("The computer wins!")
            score[0] = score[0] + 1
        # if tie, update tie
        elif result == 0:
            print("It's a tie!")
            score[1] = score[1] + 1
        # if player wins, update player score
        elif result == 1:
            print("You win!")
            score[2] = score[2] + 1

        # ask if the user wants to continue
        playAgain = continueGame()

    #if program ends
    print("You won", score[2], "times!")
    print("You tied", score[1], "times!")
    print("You lost", score[0], "times!")

    print("\nGoodbye!")


# this function displays the game rules to the user
# input: none
# output: none
def displayMenu():
    print("\nThe rules of the game are:")
    print("\tRock smashes scissors")
    print("\tScissors cut paper")
    print("\tPaper covers rock")
    print("\tIf both the choices are the same, it's a tie")

# this function randomly chooses a number to correspond to rock, paper, or scissors
# input: none
# output: integer
def getComputerChoice():
    return random.randrange(3)

# this function asks the user for their choice
# input: none
# output: integer
def getPlayerChoice():
    askAgain = True
    while askAgain:
        # ask user for input
        print("Please choose one of the following:")
        print("\t(0) rock")
        print("\t(1) paper")
        print("\t(2) scissors")
        userChoice = input("> ")

        # make sure valid input
        if userChoice == "0" or userChoice == "1" or userChoice == "2":
            return int(userChoice)
        else:
            print("\nInvalid input!\n")

# this function takes in the two integer choices to see who won
# input: 2 integers representing computer and player choice
# output: integer that represents who won (-1 pc wins; 0 tie; 1 player wins)
def playRound(computerChoice, playerChoice):
    if playerChoice == 0:
        print("You chose Rock.")
        if computerChoice == 0:
            print("The computer chose Rock.")
            return 0
        elif computerChoice == 1:
            print("The computer chose Paper.")
            print("Paper covers Rock!")
            return -1
        elif computerChoice == 2:
            print("The computer chose Scissors.")
            print("Rock smashes Scissors!")
            return 1
    elif playerChoice == 1:
        print("You chose Paper.")
        if computerChoice == 0:
            print("The computer chose Rock.")
            print("Paper covers Rock!")
            return 1
        elif computerChoice == 1:
            print("The computer chose Paper.")
            return 0
        elif computerChoice == 2:
            print("The computer chose Scissors.")
            print("Scissors cut Paper!")
            return -1
    elif playerChoice == 2:
        print("You chose Scissors.")
        if computerChoice == 0:
            print("The computer chose Rock.")
            print("Rock smashes Scissors!")
            return -1
        elif computerChoice == 1:
            print("The computer chose Paper.")
            print("Scissors cut Paper!")
            return 1
        elif computerChoice == 2:
            print("The computer chose Scissors.")
            return 0

# this function asks if the user wants to continue and returns corresponding boolean
# input: none
# output: boolean
def continueGame():
    askAgain = True
    while askAgain:
        userInput = input("Do you want to continue? (y/n) > ")
        if userInput.lower() == "y":
            return True
        elif userInput.lower() == "n":
            return False
        else:
            print("\nInvalid input\n")


main()