# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 1
# yanghyun@usc.edu

# variable to hold " to keep from having to use "\"" all the time
quotes = "\""

# get user to input string to each variable
userCountry = quotes + input("Enter a country: ") + quotes
userName = quotes + input("Enter a name: ") + quotes
userAdjective = quotes + input("Enter an adjective: ") + quotes
userVerb = quotes + input("Enter a verb in past tense: ") + quotes
userAdverb = quotes + input("Enter an adverb: ") + quotes

# user's string input is turned into int then assigned to each variable
# check for invalid inputs
userNum1 = int(input("Enter a positive whole number: "))
if userNum1 < 1:
    print("Not a positive number! Default is 3")
    userNum1 = 3
userNum2 = int(input("Enter a whole number greater than 1: "))
if userNum2 < 2:
    print("Not a positive number! Default is 4")
    userNum2 = 4
userNum3 = int(input("Enter a second whole number greater than 1: "))
if userNum3 < 2:
    print("Not a positive number! Default is 5")
    userNum3 = 5


# math operation
mathResult = quotes + str(userNum2 + userNum3) + quotes

# turn int back into strings for easier print
userNum1 = quotes + str(userNum1) + quotes
userNum2 = quotes + str(userNum2) + quotes
userNum3 = quotes + str(userNum3) + quotes

# user's string input is turned into float so that inputs like 0 is turned into 0.0
userHeight = float(input("Enter a positive number with a decimal: "))
# check for invalid input
if userHeight <= 0:
    print("Not a positive number! Default is 1.7")
    userHeight = quotes + "1.7" + quotes
else:
    userHeight = quotes + str(userHeight) + quotes


# print sentences using end="." to keep the next sentence on the same line
# use .title() in case the user does not capitalize correctly
print("Over the summer, I went to " + userCountry.title(), end=". ")
print("There, I made a friend named " + userName.title(), end=". ")
print(userName.title() + " was " + userHeight + " meters tall", end=" ")
print("and was very " + userAdjective.lower(), end=". ")
print("So we " + userVerb.lower() + " for " + userNum1 + " days", end=". ")
print("Afterwards, we had to say goodbye", end=". ")
print("But we " + userAdverb.lower() + " made plans to see each other again", end=" ")
print("over dinner with the whole family next time", end=". ")
print("Since " + userName.title() + " has " + userNum2 + " family members", end=" ")
print("and I have " + userNum3 + " family members", end=", ")
print("we reserved a table for " + mathResult + ".")
