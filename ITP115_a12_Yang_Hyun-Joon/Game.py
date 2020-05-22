# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 12
# yanghyun@usc.edu

from Human import Human
from Vampire import Vampire

def printHumans(humanlist):
    for number in range(len(humanlist)):
        print(number, humanlist[number])

def performFeeding(humanList, vamp):
    userInput = input("Please choose a number: ")
