# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 10
# yanghyun@usc.edu

class Animal(object):
    # constructor for animal object
    # input: int representing hunger, happiness, energy, age; str representing name, species
    # return: none
    def __init__(self, hungerArg, happinessArg, healthArg, energyArg, ageArg, nameArg, speciesArg):
        # make attributes public
        self.hunger = hungerArg
        self.happiness = happinessArg
        self.health = healthArg
        self.energy = energyArg
        self.age = ageArg
        self.name = nameArg
        self.species = speciesArg
    # increase animal happiness by 10, hunger by 5
    # input: none
    # return: none
    def play(self):
        self.happiness += 10
        self.hunger += 5
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger > 100:
            self.hunger = 100
        print("You played with " + self.name + " the " + self.species + "!")
    # decrease animal hunger by 10
    # input: none
    # return: none
    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print("You fed " + self.name + " the " + self.species + "!")
    # decrease animal's happiness by 20, increase health by 20
    # input: none
    # return: none
    def giveMedicine(self):
        self.happiness -= 20
        self.health += 20
        if self.happiness < 0:
            self.happiness = 0
        if self.health > 100:
            self.health = 100
        print("You gave medicine to " + self.name + " the " + self.species + "!")
    # increase animal energy by 20, age by 1
    # input: none
    # return: none
    def sleep(self):
        self.energy += 20
        self.age += 1
        if self.energy > 100:
            self.energy = 100
        print("You put " + self.name + " the " + self.species + " to sleep!")
    # special method for printing animal object
    # input: none
    # return: str with all the info about the animal
    def __str__(self):
        mystr = ""
        mystr += "Name: " + self.name + " the " + self.species + "\n"
        mystr += "Health: " + str(self.health) + "\n"
        mystr += "Happiness: " + str(self.happiness) + "\n"
        mystr += "Hunger: " + str(self.hunger) + "\n"
        mystr += "Energy: " + str(self.energy) + "\n"
        mystr += "Age: " + str(self.age)
        return mystr

# opens the csv file to create new animal objects
# input: str representing name of csv file
# return: list of animal objects
def loadAnimals(fileName):
    myFile = open(fileName, "r")
    animalList = []
    for line in myFile:
        line = line.strip()
        arg = line.split(",")
        newAnimal = Animal(int(arg[0]), int(arg[1]), int(arg[2]), int(arg[3]), int(arg[4]), arg[5], arg[6])
        animalList.append(newAnimal)

    myFile.close()

    return animalList

# displays menu
# input: none
# return: none
def displayMenu():
    print("1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep")
    print("5) Print an Animal's stats")
    print("6) View All Animals")
    print("7) Save File")
    print("8) Exit")

# print out menu with each animal's name and species
# let user choose the animal
# input: list of animals
# return: animal object
def selectAnimal(list):
    loopAgain = True
    while loopAgain:
        for index in range(len(list)):
            print("%d) %s the %s" % (index, list[index].name, list[index].species))
        # in case of invalid input
        try:
            userChoice = int(input("Please make a selection: "))
            if userChoice < 0 or userChoice >= len(list):
                print("Invalid number!")
            else:
                return list[userChoice]
        except:
            print("Please enter a number!")

# saves all the animal info into csv file
# input: animal list
# return: none
def saveAnimals(list):
    myFile = open("animals(1).csv", "w")
    for animal in list:
        animalAttributes = [str(animal.hunger), str(animal.happiness), str(animal.health),
                            str(animal.energy), str(animal.age), animal.name, animal.species]
        inputData = ",".join(animalAttributes)
        print(inputData, file=myFile)
    myFile.close()
    print("Save success!")

def main():
    loopAgain = True
    animalList = loadAnimals("animals(1).csv")

    while loopAgain:
        displayMenu()
        userChoice = input("> ")
        if userChoice == "1":
            animal = selectAnimal(animalList)
            animal.play()
        elif userChoice == "2":
            animal = selectAnimal(animalList)
            animal.feed()
        elif userChoice == "3":
            animal = selectAnimal(animalList)
            animal.giveMedicine()
        elif userChoice == "4":
            animal = selectAnimal(animalList)
            animal.sleep()
        elif userChoice == "5":
            animal = selectAnimal(animalList)
            print()
            print(animal)
            print("--------------------------------")
        elif userChoice == "6":
            for animal in animalList:
                print(animal)
                print("-------------------------------")
        elif userChoice == "7":
            saveAnimals(animalList)
        elif userChoice == "8":
            print("Goodbye!")
            loopAgain = False
        else:
            print("Invalid option!")


main()