# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 3
# yanghyun@usc.edu


##############################################################################################
# PART 2: LARGEST NUMBER

loopAgain = True


# create loop for play again
while loopAgain:

    # initialize necessary variables
    myLargest = 0
    isFirstInput = True

    # print instructions
    print("Input an integer greater than or equal to 0 or -1 to quit")

    # check for valid initial input
    # repeat if invalid
    while isFirstInput:
        userInput = int(input("> "))
        if userInput < -1:
            print("Invalid input!")
        elif userInput == -1:
            print("Must enter valid number first!")
        else:
            myLargest = userInput
            isFirstInput = False

    # loop until user input is -1
    while userInput != -1:

        userInput = int(input("> "))

        # if user input is greater than or equal to 0
        # compare to the variable
        # if input is greater then store it to the variable
        if userInput >= 0:
            if userInput > myLargest:
                myLargest = userInput
        # if user enters a negative number that is not -1
        elif userInput < -1:
            print("Invalid input! Please try again!")


    # display the largest number
    print("The largest number is", myLargest, "\n")

    # while loop for invalid input
    while userInput != "y" and userInput != "n":
        # ask if the user wants to play again
        userInput = input("Play again? (y/n) > ").lower()
        if userInput == "n":
            loopAgain = False
            print("\nGoodbye!")
        elif userInput != "y" and userInput != "n":
            print("Invalid input\n")

##############################################################################################