# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 8
# yanghyun@usc.edu

#------------------------------------------------------------------------------------------------
def main():
    fileIn = ""
    fileOut = ""
    maxResult = []
    minResult = []

    # get csv file to read from
    fileIn = whichYear()
    # get file name to output
    fileOut = askFile()

    # get all car types from csv file
    carTypes = getAllCarTypes(fileIn)

    # get user-chosen car type
    carType = getCarType(carTypes)

    # store results of calculation in list for each result
    maxResult = calcMaxMPG(carType, fileIn)
    minResult = calcMinMPG(carType, fileIn, maxResult[-1])

    # output the result into the file
    outputToFile(maxResult, minResult, fileOut, fileIn)

    print("Thanks! Have a great day!")
#------------------------------------------------------------------------------------------------
# asks which year the user would like to see the data for
# input: none
# output: string representing filename
def whichYear():
    askAgain = True
    filename = ""
    while askAgain:
        year = input("What year would you like to see the data for? (2008 or 2009): ")
        # in case user enters non integer value
        try:
            year = int(year)
            # if user enters year other than 2008 and 2009
            if year != 2008 and year != 2009:
                print("There is no data for the given year!")
            else:
                askAgain = False
        # let user know they need to enter an integer value
        except:
            print("Please enter a valid number!")
    if year == 2008:
        filename = "epaVehicleData2008.csv"
    elif year == 2009:
        filename = "epaVehicleData2009.csv"

    return filename
#------------------------------------------------------------------------------------------------
# asks user for filename to receive output
# input: none
# output: string representing filename
def askFile():
    filename = input("Enter the filename to save results to: ")
    # in case the filename does not contain ".txt" add it for them
    # get the last 4 characters
    if filename[-4:] != ".txt":
        filename = filename + ".txt"
    return filename
#------------------------------------------------------------------------------------------------
# takes the file and gets all the car types
# input: str of the filename
# output: list containing all the car types
def getAllCarTypes(filename):
    # initialize list
    rowList = []
    # initialize set
    typeSet = set()

    # open file
    myFile = open(filename, "r")

    # read the header first
    myFile.readline()
    # read each row
    for row in myFile:
        # strip row
        row = row.strip()
        # separate row into different data
        rowList = row.split(",")
        # get car type
        typeSet.add(rowList[0])

    # close file
    myFile.close()

    return typeSet
#------------------------------------------------------------------------------------------------
# lets user choose what type of car they want to see the data for
# input: a set of car types
# output: a str representing car type
def getCarType(cartypes):
    # convert set into list
    types = list(cartypes)
    count = 0
    askAgain = True

    # sort types into alphabetical order
    types.sort()

    # print the menu
    for type in types:
        count = count + 1
        print("\t", count, type)
    while askAgain:
        userChoice = input("Which car type do you want to see the data for? ")
        # in case of non integer value
        try:
            userChoice = int(userChoice)
            # invalid choice
            if userChoice < 1 or userChoice > len(cartypes):
                print("Please choose a valid option!")
            # valid choice
            else:
                askAgain = False
        except:
            print("Please enter a valid number!")
    # get user choice and return appropriate string
    return types[userChoice-1]
#------------------------------------------------------------------------------------------------
# receives car type and filename as input, calculates max highway MPG for the type
    # go through each row
    # see if car type matches
    # see if highway MPG is greater
    # if greater, store manufacturer, car line in each list
    # if same, append to list
# input: string representing car type and filename
# output: list with list of manufacturer-car line pair + max MPG value
def calcMaxMPG(cartype, filename):
    rowList = []
    mfrList = []
    carlineList = []
    max = 0
    result = []

    myFile = open(filename, "r")

    # read header
    myFile.readline()

    for row in myFile:
        row = row.strip()
        rowList = row.split(",")
        # 1st column => car type data
        # see data only for specified car type
        if rowList[0] == cartype:
            # 10th column => highway MPG data
            # if greater than current max then reset mfr and carline list
            # then add manufacturer and car line to each list
            # reset max
            if int(rowList[9]) > max:
                mfrList = []
                mfrList.append(rowList[1])
                carlineList = []
                carlineList.append((rowList[2]))
                max = int(rowList[9])
            # if same as max then just append to list
            elif int(rowList[9]) == max:
                mfrList.append(rowList[1])
                carlineList.append(rowList[2])
    # add list of manufacturer and carline to result list
    for i in range(len(mfrList)):
        result.append([mfrList[i], carlineList[i]])
    # add max MPG value
    result.append(max)

    # close file
    myFile.close()

    return result
#------------------------------------------------------------------------------------------------
# receives car type and filename as input, calculates min highway MPG for the type
    # go through each row
    # see if car type matches
    # see if highway MPG is less
    # if less, store manufacturer, car line in each list
    # if same, append to list
# input: string representing car type and filename, int representing max MPG
# output: list with list of manufacturer-car line pair + min MPG value
def calcMinMPG(cartype, filename, max):
    rowList = []
    mfrList = []
    carlineList = []
    min = max
    result = []

    myFile = open(filename, "r")

    # read header
    myFile.readline()

    for row in myFile:
        row = row.strip()
        rowList = row.split(",")
        # 1st column => car type data
        # see data only for specified car type
        if rowList[0] == cartype:
            # 10th column => highway MPG data
            # if less than current min then reset mfr and carline list
            # then add manufacturer and car line to each list
            # reset min
            if int(rowList[9]) < min:
                mfrList = []
                mfrList.append(rowList[1])
                carlineList = []
                carlineList.append((rowList[2]))
                min = int(rowList[9])
            # if same as min then just append to list
            elif int(rowList[9]) == min:
                mfrList.append(rowList[1])
                carlineList.append(rowList[2])
    # add list of manufacturer and carline to result list
    for i in range(len(mfrList)):
        result.append([mfrList[i], carlineList[i]])
    # add min MPG value
    result.append(min)

    # close file
    myFile.close()

    return result
#------------------------------------------------------------------------------------------------
# outputs min and max MPG data to file specified by user
# input: 2 lists containing max and min MPG data, str of filename, str of filename of csv
# output: none
def outputToFile(maxList, minList, filenameOut, filenameIn):
    # in case something goes wrong
    try:
        year = ""
        myFile = open(filenameOut, "w")

        if filenameIn == "epaVehicleData2008.csv":
            year = "2008"
        else:
            year = "2009"
        # print output to file
        print("EPA Highway MGP Calculator (" + year + ")", file=myFile)
        print("---------------------------------------", file=myFile)
        # print max value into file
        print("Maximum Mileage (highway):", maxList[-1], file=myFile)
        # go through the result, list all the manufacturer and car line but not the max value
        for pairList in maxList[:-1]:
            print("\t", pairList[0], pairList[1], file=myFile)
        print("---------------------------------------", file=myFile)
        # print min value into file
        print("Minimum Mileage (highway):", minList[-1], file=myFile)
        # go through the result, list all the manufacturer and car line but not the min value
        for pairList in minList[:-1]:
            print("\t", pairList[0], pairList[1], file=myFile)

        myFile.close()

        print("Operation success! Mileage data has been saved to", filenameOut)
    # notify user something went wrong
    except:
        print("Oops! Something went wrong!")
#------------------------------------------------------------------------------------------------
main()