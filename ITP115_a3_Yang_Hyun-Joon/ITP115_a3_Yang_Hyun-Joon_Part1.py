# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 3
# yanghyun@usc.edu


# import random module for use
import random

##############################################################################################
# PART 1: PIG ELVISH

# initialize necessary variables
loopAgain = True
userWord = ""
wordList = []
newWord = ""

# while loop for invalid input / play again
while loopAgain:

    # print menu
    print("Welcome to the Pig Elvish translator!")

    print("What would you like to do?")
    print("\ta) Translate English to Pig Elvish")
    print("\tb) Translate Pig Elvish to English")

    userChoice = input("> ").lower()





    # This section deals with converting English to Pig Elvish
    #--------------------------------------------------------------------------------------------

    # The user chooses to translate English to Pig Elvish
    if userChoice == "a":

        # while loop for invalid input
        while loopAgain:

            # clear previous list
            wordList = []

            # get user input
            userWord = input("\nEnter a word you would like to translate to Pig Elvish: ")

            # in case they put in multiple words
            if " " in userWord:
                print("Please enter only 1 word!")

            else:

                # turn string into list so it is mutable
                for letter in userWord:
                    wordList.append(letter)

                # add first letter to last of list then delete the first letter
                wordList.append(wordList.pop(0))

                # check for capitalization
                # make everything lowercase (will capitalize first letter later)
                isCapitalized = False
                if wordList[len(wordList)-1] == wordList[len(wordList)-1].capitalize():
                    isCapitalized = True
                for letterIndex in range(0,len(wordList)):
                    wordList[letterIndex] = wordList[letterIndex].lower()

                # count the letters
                # if less or equal to 3 then add "en"
                # if more than 3 then add random vowel
                if len(wordList) <= 3:
                    wordList = wordList + ["e","n"]
                else:
                    vowels = "aeiou"
                    wordList.append(random.choice(vowels))

                # look at each letter and see if the letter is a vowel
                # if it is a vowel then create 50:50 chance that an accent gets added
                for letterIndex in range(0,len(wordList)):
                    if wordList[letterIndex] in "aeiou":
                        if random.randrange(10) <= 4:
                            if wordList[letterIndex] == "a":
                                wordList[letterIndex] = chr(225)
                            elif wordList[letterIndex] == "e":
                                wordList[letterIndex] = chr(233)
                            elif wordList[letterIndex] == "i":
                                wordList[letterIndex] = chr(237)
                            elif wordList[letterIndex] == "o":
                                wordList[letterIndex] = chr(243)
                            else:
                                wordList[letterIndex] = chr(250)

                # if end in e then add umlaut (UTF-8 code 235)
                if wordList[len(wordList)-1] == "e" or wordList[len(wordList)-1] == chr(233):
                    wordList[len(wordList)-1] = chr(235)

                # change all "k" to "c"
                for letterIndex in range(0,len(wordList)):
                    if wordList[letterIndex] == "k":
                        wordList[letterIndex] = "c"

                # if the first letter was capitalized
                # then capitalize the first letter of new list
                if isCapitalized:
                    wordList[0] = wordList[0].capitalize()

                # print the final word as string
                newWord = "".join(wordList)
                print("\'" + userWord + "\' in Elvish is:", newWord, "\n")

                # jump to play again question
                loopAgain = False
    #--------------------------------------------------------------------------------------------



    # This section deals with reverse translation
    #----------------------------------------------------------------------------------------------

    # the user choose to translate from Pig Elvish to English
    elif userChoice == "b":
        # while loop for invalid input
        while loopAgain:

            # clear previous list
            wordList = []

            # get user input
            userWord = input("\nEnter a word you would like to translate to English: ")

            # in case they put in multiple words
            if " " in userWord:
                print("Please enter only 1 word!")

            else:

                # turn string into list so it is mutable
                for letter in userWord:
                    wordList.append(letter)

                # check for capitalization
                # make everything lowercase (will capitalize first letter later)
                isCapitalized = False
                if wordList[0] == wordList[0].capitalize():
                    isCapitalized = True
                for letterIndex in range(0, len(wordList)):
                    wordList[letterIndex] = wordList[letterIndex].lower()

                # turn the accents into normal vowels
                for letterIndex in range(0,len(wordList)):
                    if wordList[letterIndex] == chr(225):
                        wordList[letterIndex] = "a"
                    elif wordList[letterIndex] == chr(233) or wordList[letterIndex] == chr(235):
                        wordList[letterIndex] = "e"
                    elif wordList[letterIndex] == chr(237):
                        wordList[letterIndex] = "i"
                    elif wordList[letterIndex] == chr(243):
                        wordList[letterIndex] = "o"
                    elif wordList[letterIndex] == chr(250):
                        wordList[letterIndex] = "u"

                # look at the number of letters and ending to determine what to delete ("en" or vowel)
                # then delete appropriate letter(s)
                # if neither "en" nor vowel, the word is not Elvish
                # so go back to asking for the word
                if len(wordList) <= 5 and wordList[len(wordList)-2:len(wordList)] == ["e", "n"]:
                    del wordList[len(wordList)-2:len(wordList)]
                elif len(wordList) > 5 and wordList[len(wordList)-1] in "aeiou":
                    del wordList[len(wordList)-1]
                else:
                    print("Looks like the word is not Elvish!")
                    continue

                # get the last letter and put it first
                lastLetter = wordList[len(wordList)-1]
                for letterIndex in range(len(wordList)-1, 0, -1):
                    wordList[letterIndex] = wordList[letterIndex - 1]
                wordList[0] = lastLetter

                # turn all "c"s into "k"s
                # NOTE
                    # you are NOT guaranteed to get the original word back since you do not know
                    # whether the "c" in Elvish is supposed to be "k" or remain as "c"
                for letterIndex in range(0,len(wordList)):
                    if wordList[letterIndex] == "c":
                        wordList[letterIndex] = "k"

                # if the first letter was capitalized
                # then capitalize the first letter of new list
                if isCapitalized:
                    wordList[0] = wordList[0].capitalize()

                # print the final word as string
                newWord = "".join(wordList)
                print("\'" + userWord + "\' in English is:", newWord)
                print("*** Please note that the word may NOT be the EXACT translation!***\n")

                # jump to play again question
                loopAgain = False
    #----------------------------------------------------------------------------------------------



    else:
        print("Invalid input!\n")

        # jump back to the top
        continue

    # ask user if he wants to play again
    # if yes start over
    # if no goodbye
    loopAgain = True
    while loopAgain:
        userChoice = input("Play again? (y/n) > ").lower()
        if userChoice == "y":
            print("\n")
            # break out of this loop to start from the top
            break
        elif userChoice == "n":
            # set loopAgain to false to run rest of code for exit
            loopAgain = False
        else:
            print("Invalid input!\n")


# print goodbye
print("\nOodbyega! Aveha aen icen" + chr(233), "ayden!")
print("Goodbye! Have a nice day!")
####################################################################################################