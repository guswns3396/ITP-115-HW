# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 12
# yanghyun@usc.edu

from Being import Being

class Human(Being):
    def __init__(self, name, quarts, bloodType):
        super().__init__(name, quarts)
        self.__bloodType = bloodType

    def getBloodType(self):
        return self.__bloodType
    def setBloodType(self, bloodType):
        self.__bloodType = bloodType

    def isAlive(self):
        if self.__quarts > 0:
            return True
        else:
            return False

    def __str__(self):
        msg = "Human " + self.getName() + " has " + str(self.getQuarts()) + " quarts of "
        msg += "type " + self.__bloodType + " blood."
        return msg

