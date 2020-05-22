# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 4
# yanghyun@usc.edu


##############################################################################################
# PART 1: WORD JUMBLE GAME

# import required module
import random

# initialize necessary variables
wordList = []
hintList = []
guessCount = 0
score = 0
loopAgain = True
answer = ""
jumbledList = []
wordLetters = []
gaveHint = False

# print welcome
print("Welcome to the Word Jumble Game\n")

# loop for play again, etc
while loopAgain:

    # print menu
    print("Please select one of the following:")
    print("\ta) Add words")
    print("\tb) Play!")
    print("\tc) Quit")

    # get user input
    userInput = input("> ").lower()


    # if user chooses to add words
    if userInput == "a":

        # loop for repeat
        while loopAgain:
            # get user input and add to list
            userInput = input("\nPlease input a word: ").lower()
            wordList.append(userInput)
            # get hint for the word
            userInput = input("Please input the hint for the word: ").capitalize()
            hintList.append(userInput)

            # loop for invalid input
            while loopAgain:
                # ask the user if they want to add another
                userInput = input("Add another word? (y/n): ").lower()
                if userInput == "y":
                    break
                elif userInput == "n":
                    loopAgain = False
                # in case for invalid input
                else:
                    print("Invalid input!")

        loopAgain = True


    # if user chooses to play
    elif userInput == "b":
        # if there are no words in the list
        if not wordList:
            print("No words added!\n")
        else:
            # pick a random word from list of words
            answer = random.choice(wordList)
            # turn the answer into a list
            wordLetters = list(answer)
            # empty jumbled list
            jumbledList = []

            # jumble word
            #--------------------------------------------------------------------
            # while there are still letters in the list of letters
            while wordLetters:
                # pick a random index from the list
                letterIndex = random.randrange(len(wordLetters))
                # store into temporary variable and delete letter from list
                letter = wordLetters.pop(letterIndex)
                # add the letter into jumbled list
                jumbledList.append(letter)
            #---------------------------------------------------------------------

            # start guessing
            #--------------------------------------------------------------------
            # while loop to keep guessing
            while loopAgain:
                # print jumbled word as string and have the user guess
                print("".join(jumbledList))
                myInput = input("Please take a guess: ").lower()

                # check if correct, notify the user
                if myInput == answer:
                    guessCount = guessCount + 1
                    print("Correct! Great job!\n")
                    print("You took", guessCount, "tries!")

                    # calculate score
                    #--------------------------------------------------------------------------
                    if guessCount == 1:
                        print("You earned 10 points!")
                        score = score + 10
                    elif guessCount == 2:
                        print("You earned 8 points!")
                        score = score + 8
                    elif guessCount == 3:
                        print("You earned 6 points!")
                        score = score + 6
                    else:
                        print("You earned 3 points!")
                        score = score + 3
                    # if hint was not used give bonus
                    if not gaveHint:
                        score = score + 2
                        print("You earned extra 2 points for not using the hint!")

                    # display score
                    print("You currently have", score, "points!")

                    loopAgain = False
                    gaveHint = False
                    guessCount = 0

                else:
                    guessCount = guessCount + 1
                    print("Incorrect! Please try again!\n")
                    # ask for hint
                    #-------------------------------------------------------------------------
                    while not gaveHint:
                        # ask if user wants a hint
                        userInput = input("Would you like a hint? (y/n): ").lower()
                        if userInput == "y":
                            # find position of answer in word list
                            # use the index to find corresponding hint
                            index = wordList.index(answer)
                            hint = hintList[index]
                            # display hint
                            print(hint)
                            # set the variable to true to mark that user got a hint
                            gaveHint = True
                        elif userInput == "n":
                            break
                        else:
                            print("Invalid input!")
                    #--------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------

        loopAgain = True

    # if user chooses to quit
    elif userInput == "c":
        print("Goodbye!")
        loopAgain = False

    # If invalid input
    else:
        print("Invalid input!")


######################################################################################################