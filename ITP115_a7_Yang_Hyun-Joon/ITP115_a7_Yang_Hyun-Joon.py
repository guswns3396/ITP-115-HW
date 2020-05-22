# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 7
# yanghyun@usc.edu

# importing helper file
import TicTacToeHelper

def main():
    playAgain = True
    userInput = ""

    # while loop to keep playing
    while playAgain:
        print("Welcome to Tic Tac Toe!")
        playGame()

        # ask user if play again
        while userInput != "y" and userInput != "n":
            userInput = input("Play again? (y/n) > ").lower()
            if userInput != "y" and userInput != "n":
                print("Invalid input!")
        if userInput == "y":
            userInput = ""
            continue
        else:
            print("Goodbye!")
            playAgain = False

# takes in board list and prints the board in a prettier format
# input: board list
# output: none
def printPrettyBoard(board_list):
    print()
    counter = 0
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(board_list[counter], end=" | ")
            else:
                print(board_list[counter])
            counter += 1
        if i < 2:
            print("----------")
    print()

# given the board and the chosen spot, this function determines whether it is a valid move
# input: list representing the board; int representing the spot on the board
# output: boolean whether the move is valid (true) or not (false)
def isValidMove(boardList, spot):
    if spot >= 0 and spot < 9:
        if boardList[spot] == "x" or boardList[spot] == "o":
            return False
        else:
            return True
    else:
        return False

# takes current board list and places player's letter in the specified spot
# input: list representing board, int representing the spot, string presenting player's letter
# output: none
def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter

# initialize the list representing board to a list of strings from 0-8
# keep track of moves that have been made using a counter
# use while loop to allow player to make moves until game ends
# ask current player for move
# check if game ended
# print out result
def playGame():
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    counter = 0
    player = ""
    playerMark = ""
    playerSpot = 0
    loopAgain = True

    # continue as long as game has not ended
    while TicTacToeHelper.checkForWinner(board, counter) == "n":

        # for alternating players
        if counter % 2 == 0:
            player = "Player 1"
            playerMark = "o"
        else:
            player = "Player 2"
            playerMark = "x"

        # get player's move after printing board
        # while loop for invalid input
        while loopAgain:
            # try and except for non int input
            try:
                # print board
                printPrettyBoard(board)

                # get player's move
                print("It is " + player + "'s turn!")
                playerSpot = int(input("Please choose a number to make a move: "))
                isValidMove(board, playerSpot)

            except:
                print("\nPlease enter a valid number!\n")

            else:
                # determine whether to loop again or not
                loopAgain = not isValidMove(board, playerSpot)
                if loopAgain:
                    print("\nInvalid input!\n")

        # reset loop variable
        loopAgain = True

        # update board
        updateBoard(board, playerSpot, playerMark)

        # update counter
        counter = counter + 1

    # game over
    # display result
    printPrettyBoard(board)
    print("Game over!")
    if TicTacToeHelper.checkForWinner(board, counter) == "s":
        print("It's a tie!")
    elif TicTacToeHelper.checkForWinner(board, counter) == "x":
        print("Player 2 wins!")
    elif TicTacToeHelper.checkForWinner(board, counter) == "o":
        print("Player 1 wins!")



main()