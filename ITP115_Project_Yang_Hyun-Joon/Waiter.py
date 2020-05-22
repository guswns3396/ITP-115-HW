# import necessary files
from Menu import Menu
from Diner import Diner

# create Waiter class
class Waiter(object):
    # constructor
    # input: Menu object
    # return: none
    def __init__(self, menu):
        self.__diners = []
        self.__menu = menu

    # add new Diner object to waiter's list of diners
    # input: Diner object
    # return: none
    def addDiner(self, diner):
        self.__diners.append(diner)

    # returns number of diners the waiter is keeping track of
    # input: none
    # return: int representing number of diners
    def getNumDiners(self):
        return len(self.__diners)

    # prints all the diners the waiter is keeping track of, grouped by status
    # input: none
    # return: none
    def printDinerStatuses(self):
        # loop through each status
        for status in Diner.STATUSES:
            print(status.upper() + ":")
            # loop through diner list
            for diner in self.__diners:
                # if diner's status matches the corresponding status
                # print diner's name
                if Diner.STATUSES[diner.getStatus()] == status:
                    print("\t" + diner.getName())
            print("--------------")
        print("\n")

    # simulate taking orders
    # input: none
    # return: none
    def takeOrders(self):
        # variable for list of diners ordering
        orderingDiners = []
        # loop through the list of diners to check if diner is "ordering"
        for diner in self.__diners:
            if diner.getStatus() == 1:
                orderingDiners.append(diner)
        for diner in orderingDiners:
            # loop through each menu type
            for menuType in Menu.MENU_ITEM_TYPES:
                # print all the items in menu type
                self.__menu.printMenuItemsByType(menuType)
                # ask diner to pick item from menu type then add to diner's order then print order
                loopAgain = True
                while loopAgain:
                    # for error checking
                    try:
                        order = int(input("What " + menuType.lower() + " would you like to order, "
                                          + diner.getName() + "? "))
                        if order > 0 and order <= len(menuType):
                            item = self.__menu.getMenuItem(menuType, order-1)
                        else:
                            raise ValueError("Invalid index")
                        diner.addToOrder(item)
                        loopAgain = False
                    except:
                        print("Please choose a valid item!")
            diner.printOrder()
            print("\n")

    # if diner's paying, calculate meal cost and print it out in a message
    # input: none
    # return: none
    def ringUpDiners(self):
        # variable for list of paying diners
        payingDiners = []
        # loop through the list of diners to check if diner's paying
        for diner in self.__diners:
            if diner.getStatus() == 3:
                payingDiners.append(diner)
        # loop through paying diners and calculate meal cost
        for diner in payingDiners:
            print("The total for " + diner.getName() + " is $" + str(diner.calculateMealCost()))

    # for each diner that is leaving, thank them and remove them from list
    # input: none
    # return: none
    def removeDoneDiners(self):
        # loop through the list of diners backwards to check if diner's leaving
        for index in range(0, len(self.__diners)):
            diner = self.__diners[len(self.__diners)-1-index]
            # if leaving, thank them and remove them from list
            if diner.getStatus() == 4:
                print("Thank you for coming, " + diner.getName() + "!")
                del self.__diners[len(self.__diners)-1-index]

    # allow the waiter to attend to the diners at their various stages
    # as well as move each diner on to the next stage
    # input: none
    # return: none
    def advanceDiners(self):
        # print all the diners of the waiter according to status
        self.printDinerStatuses()
        # take orders of diners that are ordering
        self.takeOrders()
        # calculate cost of meal for diners that are paying
        self.ringUpDiners()
        # thank and remove diners that are leaving
        self.removeDoneDiners()
        # update each diner's status
        for diner in self.__diners:
            diner.updateStatus()

############################################################################################
'''
#test
def main():
    menu = Menu("menu.csv")
    waiter = Waiter(menu)
    diner1 = Diner("Jack")
    waiter.addDiner(diner1)
    waiter.printDinerStatuses()
main()
'''