# create MenuItem class that does not inherit from another class
class MenuItem(object):

    # define the constructor with necessary inputs
    # inputs: str for name, str for item type, float for price, str for description
    def __init__(self, name, itemType, price, description):
        # create necessary private variables
        self.__name = name
        self.__type = itemType
        self.__price = price
        self.__description = description

    # getters for private variables
    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
    def getPrice(self):
        return self.__price
    def getDescription(self):
        return self.__description

    # setters for private variables
    def setName(self, name):
        self.__name = name
    def setType(self, itemType):
        self.__type = itemType
    def setPrice(self, price):
        self.__price = price
    def setDescription(self, description):
        self.__description = description

    # special behavior for printing the class
    def __str__(self):
        msg = self.__name + " (" + self.__type + "): $" + "{:.2f}".format(self.__price)
        msg += "\n\t" + self.__description
        return msg