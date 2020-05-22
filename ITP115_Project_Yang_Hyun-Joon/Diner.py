# import MenuItem class for use
from MenuItem import MenuItem

# create a new class Diner
class Diner(object):

    # class variable for list of strings representing status of diner
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # constructor for Diner class
    # input: str for name
    # return: none
    def __init__(self, name):
        self.__name = name
        self.__order = []
        self.__status = 0

    # getters for instance attributes
    def getName(self):
        return self.__name
    def getOrder(self):
        return self.__order
    def getStatus(self):
        return self.__status

    # setters for instance attributes
    def setName(self, name):
        self.__name = name
    def setOrder(self, order):
        self.__order = order
    def setStatus(self, status):
        self.__status = status

    # increase diner's status by 1
    # input: none
    # return: none
    def updateStatus(self):
        self.__status += 1

    # add menu item to the end of the list of menu items
    # input: MenuItem object
    # return: none
    def addToOrder(self, menuItem):
        self.__order.append(menuItem)

    # prints msg containing all the menu items the diner ordered
    # input: none
    # return: none
    def printOrder(self):
        print(self.__name, "has ordered:")
        for item in self.__order:
            print("\t", item.getName())

    # calculates cost of the meal
    # input: none
    # return: float for total cost of meal
    def calculateMealCost(self):
        cost = 0
        for item in self.__order:
            cost += item.getPrice()
        return cost

    # special method to print message containing diner's name and status
    # input: none
    # return: none
    def __str__(self):
        msg = "Diner " + self.__name + " is currently " + Diner.STATUSES[self.__status] + "."
        return msg

##############################################################################
'''
#test
def main():
    myDiner = Diner("Jack")
    myMenuItem1 = MenuItem("Ice Cream","Dessert",3.50,"3 scoops of chocolate or vanilla or strawberry")
    myMenuItem2 = MenuItem("Ice Cream2", "Dessert", 3.30, "3 scoops of chocolate or vanilla or strawberry")
    myDiner.setOrder([myMenuItem1])
    myDiner.printOrder()
    myDiner.addToOrder(myMenuItem2)
    myDiner.printOrder()
    print(myDiner.calculateMealCost())
    print(myDiner)
    myDiner.updateStatus()
    print(myDiner)
main()
'''