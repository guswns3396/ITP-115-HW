# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 12
# yanghyun@usc.edu

from Being import Being

class Vampire(Being):
    MAX_BLOOD = 5
    HUNGER_LEVELS = ["starving", "hangry", "hungry", "content", "full", "stuffed"]

    def __init__(self, name, quarts, animalForm):
        super().__init__(name, quarts)
        self.__animalForm = animalForm

    def getAnimalForm(self):
        return self.__animalForm
    def setAnimalForm(self, animalForm):
        self.__animalForm = animalForm

    def getHunger(self):
        return Vampire.HUNGER_LEVELS[self.__quarts]

    def isStuffed(self):
        if self.__quarts == Vampire.MAX_BLOOD:
            return True
        else:
            return False

    def suckBlood(self, human):
        if self.__quarts < 5:
            self.increaseQuarts()
        human.decreaseQuarts()

    def __str__(self):
        msg = "Count " + self.getName() + " is " + self.getHunger()
        return msg