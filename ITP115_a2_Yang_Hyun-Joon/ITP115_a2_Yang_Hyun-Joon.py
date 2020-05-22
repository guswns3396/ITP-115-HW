# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 2
# yanghyun@usc.edu


##################################################################################################
# PART 1: HARRY POTTER VENDING MACHINE


# initialize price and name variables
menuName = ""
menuPrice = 0

# initialize repeat variable
repeat = True


# THIS SECTION DEALS WITH USER'S MENU CHOICE
#-------------------------------------------------------------------------

# create a while loop in case of invalid option
while repeat:

    # print the menu
    print("Please select an item from the vending machine:")
    print("\ta) Butterbeer: 58 knuts")
    print("\tb) Quill: 10 knuts")
    print("\tc) The Daily Prophet: 7 knuts")
    print("\td) Book of Spells: 400 knuts")

    # store choice into variable; use .lower() to consider capitalization
    userChoice = input("> ").lower()

    if userChoice == "a":
        menuName = "Butterbeer"
        menuPrice = 58
        repeat = False
    elif userChoice == "b":
        menuName = "Quill"
        menuPrice = 10
        repeat = False
    elif userChoice == "c":
        menuName = "The Daily Prophet"
        menuPrice = 7
        repeat = False
    elif userChoice == "d":
        menuName = "Book of Spells"
        menuPrice = 400
        repeat = False
    else:
        print("Invalid option! Please choose a valid option!\n")
#-----------------------------------------------------------------------------




# Verify choice
print("You have chosen menu", userChoice, ":", menuName, "for", menuPrice, "knuts!")

# set repeat to true again for next while loop
repeat = True



# THIS SECTION DEALS WITH DISCOUNT
#------------------------------------------------------------------------------------------

# create a while loop in case of invalid option
while repeat:
    # Ask if user wants discount; use .lower() in case of capitalization
    userChoice = input("Would you like to share this on Instagram for a discount of 5 knuts? (y/n) > ").lower()

    if userChoice == "y":
        menuPrice = menuPrice - 5
        print("Thanks! Your price is now", menuPrice, "knuts\n")
        repeat = False
    elif userChoice == "n":
        print("Okay! Your price will be", menuPrice, "\n")
        repeat = False
    else:
        print("Invalid choice! Please choose a valid option!\n")
#------------------------------------------------------------------------------------------




# THIS SECTION DEALS WITH TRANSACTION
#-----------------------------------------------------------------------------------------------

# initialize variables for each coin
print("Please input how many coins you are inserting!")
numGalleons = int(input("How many galleons? "))
numSickles = int(input("How many sickles? "))
numKnuts = int(input("How many knuts? "))


# verify
print("You've inserted", numGalleons, "galleons,", numSickles, "sickles, and", numKnuts, "knuts!")

# calculate change
change = ((numGalleons * 493) + (numSickles * 29) + numKnuts) - menuPrice

if change < 0:
    print("Sorry! You don't have enough to purchase the item!")
elif change == 0:
    print("You don't have any change!")
else:
    numGalleons = change // 493
    change = change % 493
    numSickles = change // 29
    change = change % 29
    numKnuts = change

    print("Your change is:", numGalleons, "galleons,", numSickles, "sickles, and", numKnuts, "knuts!")
#-------------------------------------------------------------------------------------------------------------


###########################################################################################################









################################################################################################
# PART 2: CHOOSE YOUR OWN ADVENTURE

# initialize variable for while loop
repeat2 = True

# set up for question 1
print("After a long week, it's finally Saturday!", end=" ")
print("You have the whole day to yourself before you have to start work again tomorrow.", end=" ")
print("You wake up in the morning to find that the weather outside is beautiful.", end=" ")
print("As you yawn, you wonder what you want to do the rest of the day...")

# while loop to consider invalid input
while repeat2:
    # question 1
    print("Do you:")
    print("\ta) Sleep in")
    print("\tb) Wake up and get started on the day")

    # get user choice
    userChoice = input("> ").lower()

    # branches for question 1
    if userChoice == "a":
            # set up for 1-a question
        print("You decide to sleep some more and after several more hours of sleep,", end=" ")
        print("you feel well rested. Then you check your phone and realize", end=" ")
        print("your friends have been trying to reach you.", end=" ")
        print("From the texts, it seems like your friends all went out without you. :(")

        # while loop for invalid input
        while repeat2:
            # 1-a question
            print("Do you:")
            print("\ta) Try calling your friends")
            print("\tb) Start watching a movie on your laptop")
            print("\tc) Get started on homework early")
            userChoice = input("> ").lower()

            # branches for 1-a
            if userChoice == "a":
                repeat2 = False
                print("You call your friends and it turns out they are heading back soon.", end=" ")
                print("You make plans to see them when they get back and hang out for the night!")
            elif userChoice == "b":
                repeat2 = False
                print("You're pretty bummed out so you decide to do something yourself.", end=" ")
                print("So you scroll through Netflix to see what you want to watch,", end=" ")
                print("but you end up watching 'The Office' again for the 100th time...")
            elif userChoice == "c":
                repeat2 = False
                print("You judge that the day will be over soon", end=" ")
                print("so you decide you might as well get started on the homework early.", end=" ")
                print("Your roommate calls you a nerd for doing homework on a Saturday,", end=" ")
                print("but you ignore him along with the fact that you live alone...")
            else:
                print("Invalid input! Please try again!\n")


    elif userChoice == "b":
        # set up for 1-b question
        print("You decide to wake up and get going with your day,", end=" ")
        print("so you make yourself some breakfast. As you finish your breakfast,", end=" ")
        print("you get a text from your friend saying they want to go to Santa Monica!")

        # while loop for invalid input
        while repeat2:
            # 1-b question
            print("Do you:")
            print("\ta) Reply saying you want to go")
            print("\tb) Reply saying you want to go to the Griffith Observatory instead")
            print("\tc) Stay home")
            userChoice = input("> ").lower()

            # branches for 1-b
            if userChoice == "a":
                repeat2 = False
                print("You tell your friends you want to go and make plans accordingly.", end=" ")
                print("You spend an amazing day at the beach and", end=" ")
                print("even though you got a nasty sunburn, you decide it was all worth it!")
            elif userChoice == "b":
                repeat2 = False
                print("You convince your hesitant friends to go to the Griffith Observatory instead.", end=" ")
                print("But when you arrive at the Observatory, you find the place is closed", end=" ")
                print("due to a movie filming. They tell you the movie's called 'La La Land'.", end=" ")
                print("You think 'what a dumb movie' and promise yourself never to watch it when it comes out.")
            elif userChoice == "c":
                repeat2 = False
                print("You decide you don't want to hang out with your friends,", end=" ")
                print("but would rather do some python programming!", end=" ")
                print("Honestly, who needs friends when you can code python! Am I right??")
            else:
                print("Invalid input! Please try again!\n")


    else:
        print("Invalid input! Please try again!\n")
########################################################################################################################