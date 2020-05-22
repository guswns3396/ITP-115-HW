# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 12
# yanghyun@usc.edu

class Being(object):
    def __init__(self, name, quarts):
        self.__name = name
        self.__quarts = quarts

    def getName(self):
        return self.__name
    def getQuarts(self):
        return self.__quarts
    def setName(self, name):
        self.__name = name
    def setQuarts(self, quarts):
        self.__quarts = quarts

    def increaseQuarts(self):
        self.__quarts += 1
    def decreaseQuarts(self):
        self.__quarts -= 1