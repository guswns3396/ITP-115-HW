# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 11
# yanghyun@usc.edu

class Superhero(object):
    # constructor for Superhero class
    # input: str for name, str for type, int for attack
    # return: none
    def __init__(self, name, type, attack):
        self.__name = name
        self. __type = type
        self.__attack = attack
        self.__health = 100
    # gets the superhero's name
    # input: none
    # return: str of name
    def getName(self):
        return self.__name
    # gets the superhero's attack value
    # input: none
    # return: int representing attack value
    def getAttack(self):
        return self.__attack
    # gets the health of the superhero
    # input: none
    # return: int representing health
    def getHealth(self):
        return self.__health
    # gets superhero's type
    # input: none
    # return: string representing hero or villain
    def getType(self):
        return self.__type
    # decrease superhero's health by opponent's attack value
    # input: int representing opponent attack value
    # return: none
    def loseHealth(self, attack):
        self.__health -= attack
    # decides whether or not the hero's dead
    # input: none
    # return: boolean representing whether the hero's dead
    def isDead(self):
        if self.__health <= 0:
            return True
        else:
            return False
    # special behavior for printing hero's info
    # input: none
    # return: str regarding hero's info
    def __str__(self):
        msg = self.__name + " the " + self.__type + " has " + str(self.__attack)
        msg += " attack points and currently has " + str(self.__health) + " health points."
        return msg
