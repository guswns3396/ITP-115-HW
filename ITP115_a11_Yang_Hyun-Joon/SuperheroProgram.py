# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 11
# yanghyun@usc.edu

from Superhero import Superhero

# asks user questions to create superhero instance
# input: none
# return: list of Superhero instances
def createHero():
    name = ""
    type = ""
    attack = 0
    loopAgain = True
    superheroList = []

    # create 2 superheros
    for index in range(2):

        # ask for name
        userInput = input("Enter fighter #" + str(index + 1) + "'s name: ")
        name = userInput

        # ask for hero or villain
        userInput = ""
        while userInput != "hero" and userInput != "villain":
            userInput = input("Is figher #" + str(index + 1) + " a hero or a villain?: ").lower()
            if userInput != "hero" and userInput != "villain":
                print("Invalid input!")
            else:
                type = userInput

        # ask for attack points
        while loopAgain:
            userInput = input("Enter figher #" + str(index + 1) + "'s attack points: ")
            try:
                attack = int(userInput)
                loopAgain = False
            except:
                print("Must enter a valid number!")
        loopAgain = True

        # create superhero and add to list
        hero = Superhero(name, type, attack)
        superheroList.append(hero)

    return superheroList

# simulates one round of fight of the two heros
# input: 2 superhero objects
# return: none
def fight(hero1, hero2):
    hero1.loseHealth(hero2.getAttack())
    hero2.loseHealth(hero1.getAttack())

def main():
    playAgain = True

    while playAgain:
        # store instances of hero
        heroList = createHero()
        player1 = heroList[0]
        player2 = heroList[1]

        # print out the details of each fighter
        print("\n")
        print(player1)
        print(player2)

        print("\nSTART BATTLE!\n")

        # simulate fighting until one of the player is dead
        round = 1
        while not player1.isDead() and not player2.isDead():
            print("=====", "Round", round, "=====")
            fight(player1, player2)
            print(player1)
            print(player2)
            round += 1
            print("\n")

        # tell user who won
        if player1.isDead() and player2.isDead():
            print("It's a tie!")
        elif player1.isDead():
            print(player2.getName(), "won!")
        elif player2.isDead():
            print(player1.getName(), "won!")

        # ask user if play again
        while playAgain:
            userInput = input("Play again? (y/n): ").lower()
            if userInput == "y":
                break
            elif userInput == "n":
                print("Goodbye!")
                playAgain = False
            else:
                print("Invalid input!")

main()
