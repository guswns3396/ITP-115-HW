# import MenuItem python file for use
from MenuItem import MenuItem

# create Menu class that does not inherit from another class
class Menu(object):

    # class variable
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # define constructor with necessary inputs
    # input: string representing name of csv file
    # returns: none
    def __init__(self, csvFileName):
        # empty dictionary
        self.__menuItemDictionary = {}
        # open file
        myFile = open(csvFileName, "r")
        # read each line of csv
        for line in myFile:
            # strip line & split the line into separate strings stored in list called args
            line = line.strip()
            args = line.split(",")
            # create variables for appropriate input
            name = args[0]
            itemType = args[1]
            price = float(args[2])
            desc = args[3]
            # create menuItem
            myMenuItem = MenuItem(name, itemType, price, desc)
            # add item to appropriate item type
            if itemType in self.__menuItemDictionary:
               self.__menuItemDictionary[itemType].append(myMenuItem)
            else:
               self.__menuItemDictionary[itemType] = [myMenuItem]
        # close file
        myFile.close()

    # returns the correct MenuItem from dictionary using its type and index position
    # input: str representing itemType, int representing index position
    # return: MenuItem object from dictionary
    def getMenuItem(self, itemType, index):
        return self.__menuItemDictionary[itemType][index]

    # prints a header with the type of menu items,
    # followed by a numbered list of all the menu items of that type
    # input: str representing itemType
    # return: none
    def printMenuItemsByType(self, itemType):
        print(itemType)
        print("--------------------------")
        # loop through each item of the itemType
        for i in range(0, len(self.__menuItemDictionary[itemType])):
            print(str(i+1) + ")", self.__menuItemDictionary[itemType][i])
        print("\n")

    # returns number of MenuItem objects given the menu item
    # input: str representing type of menu item
    # return: int representing number of MenuItem objects of the input type
    def getNumMenuItemsByType(self, itemType):
        return len(self.__menuItemDictionary[itemType])
############################################################################################
'''
#test
def main():
    myMenu = Menu("menu.csv")
    for itemType in Menu.MENU_ITEM_TYPES:
        myMenu.printMenuItemsByType(itemType)
    for itemType in Menu.MENU_ITEM_TYPES:
        print(myMenu.getNumMenuItemsByType(itemType))
main()
'''



