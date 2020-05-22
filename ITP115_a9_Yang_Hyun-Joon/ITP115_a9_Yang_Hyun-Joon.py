# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 9
# yanghyun@usc.edu

import random
import MusicLibraryHelper

def main():
    playAgain = True

    # import data into dictionary
    musicLibDict = MusicLibraryHelper.loadLibrary("musicLibrary.dat")

    while playAgain:
        # display menu
        displayMenu()
        # get user input
        userInput = input("> ")
        # run corresponding function
        if userInput == "1":
            displayLibrary(musicLibDict)
        elif userInput == "2":
            displayArtists(musicLibDict)
        elif userInput == "3":
            addAlbum(musicLibDict)
        elif userInput == "4":
            if deleteAlbum(musicLibDict):
                print("Delete album success!")
            else:
                print("Delete album failed!")
        elif userInput == "5":
            if deleteArtist(musicLibDict):
                print("Delete artist success!")
            else:
                print("Delete artist failed!")
        elif userInput == "6":
            searchLibrary(musicLibDict)
        elif userInput == "7":
            generateRandomPlaylist(musicLibDict)
        elif userInput == "8":
            generateCustomPlaylist(musicLibDict)
        elif userInput == "9":
            print("Saving music library...")
            MusicLibraryHelper.saveLibrary("musicLibrary.dat", musicLibDict)
            playAgain = False
        else:
            print("Invalid input!")

# print out the menu options to the user
# input: none
# return: none
def displayMenu():
    print("\nWelcome to Your Music Library")
    print("Options:")
    print("\t1) Display library")
    print("\t2) Display all artists")
    print("\t3) Add an album")
    print("\t4) Delete an album")
    print("\t5) Delete an artist")
    print("\t6) Search library")
    print("\t7) Generate a random playlist")
    print("\t8) Make your own playlist")
    print("\t9) Exit")

# print out entire music library
# input: dictionary of music library
# return: none
def displayLibrary(musicLibDictionary):
    # iterate through each key (artist) in the dictionary
    for key in musicLibDictionary:
        print("Artist: ", key)
        print("Albums:")
        # iterate through each element (album) in the list
        for album in musicLibDictionary[key]:
            print("\t- ", album)

# print out all the artists currently in user's library
# input: dictionary of music library
# return: none
def displayArtists(musicLibDictionary):
    print("Displaying all artists:")
    # iterate through each key (artist) in dictionary
    for artist in musicLibDictionary:
        print("\t- ", artist)

# ask user for artist & album then add to the library
# input: dictionary of music library
# return: none
def addAlbum(musicLibDictionary):
    # ask user for name of artist & album
    artistName = input("Enter artist: ").title()
    albumName = input("Enter album: ").title()

    # if artist already in library
    if artistName in musicLibDictionary:
        # if album already in library notify user
        if albumName in musicLibDictionary[artistName]:
            print("Album already in the library!")
        # if not add to list
        else:
            musicLibDictionary[artistName].append(albumName)
    # if artist not in library, create new item in library
    else:
        musicLibDictionary[artistName] = [albumName]

# delete album from the library
# input: dictionary of music library
# return: boolean whether album successfully deleted
def deleteAlbum(musicLibDictionary):
    # ask user for name of artist & album
    artistName = input("Enter artist: ").title()
    albumName = input("Enter album: ").title()

    # check if artist in library
    if artistName in musicLibDictionary:
        # check if album in list
        # if yes, delete album
        # if no, notify user
        if albumName in musicLibDictionary[artistName]:
            musicLibDictionary[artistName].remove(albumName)
            # if there is no album for artist, delete artist
            if not musicLibDictionary[artistName]:
                del musicLibDictionary[artistName]
            return True
        else:
            return False
    else:
        return False

# delete artist from library
# input: dictionary of music library
# return: boolean whether artist was successfully deleted
def deleteArtist(musicLibDictionary):
    # ask user for name of artist
    artistName = input("Enter artist: ").title()

    # if artist found
    if artistName in musicLibDictionary:
        # delete artist
        del musicLibDictionary[artistName]
        return True
    # if artist not found
    else:
        return False

# give user input, search for term in artists and albums
# input: string of search term
# return: none
def searchLibrary(musicLibDictionary):
    # artist & album list
    artistSearch = []
    albumSearch = []

    # ask user for search term
    searchTerm = input("Please enter a search term: ")

    # iterate through the artists
    for artist in musicLibDictionary:
        # if search term contained in artist name, append to artist list
        if searchTerm.lower() in artist.lower():
            artistSearch.append(artist)
        # iterate through albums by artist
        for album in musicLibDictionary[artist]:
            # if search term contained in album name, append to album list
            if searchTerm.lower() in album.lower():
                albumSearch.append(album)

    # print out the search result
    print("Artists containing '%s'" % searchTerm)
    # if list empty
    if not artistSearch:
        print("\tNo results")
    else:
        for artist in artistSearch:
            print("- %s" % artist)
    print("Albums containing '%s'" % searchTerm)
    # if list empty
    if not albumSearch:
        print("\tNo results")
    else:
        for album in albumSearch:
            print("- %s" % album)

# generate random playlist
# input: dictionary of music library
# return: none
def generateRandomPlaylist(musicLibDicitonary):
    # playlist dictionary
    playlist = {}

    # artist list
    artistList = []
    for artist in musicLibDicitonary:
        artistList.append(artist)

    # while artistList is not empty
    while artistList:
        index = 0
        randomArtist = ""
        randomAlbum =""
        albumList = []

        # get random index for artist
        index = random.randrange(len(artistList))
        # get random artist and delete from artist list
        randomArtist = artistList.pop(index)
        # create list of albums for randomly picked artist
        for album in musicLibDicitonary[randomArtist]:
            albumList.append(album)
        # get random index for album
        index = random.randrange(len(albumList))
        # get random album by the random artist
        randomAlbum = albumList[index]
        # artist-album dictionary pair for the randomly picked artist
        playlist[randomArtist] = randomAlbum

    # print playlist
    print("Here is your random playlist:")
    for artist in playlist:
        print("- %s by %s" % (playlist[artist], artist))

# let the user create a custom playlist
# input: dictionary of music library
# return: none
def generateCustomPlaylist(musicLibDictionary):
    loopAgain = True
    currentPlaylist = []
    counter = 0
    pickedArtist = ""
    pickedAlbum = ""
    artistList = []
    albumList = []

    # create list of artists
    for artist in musicLibDictionary:
        artistList.append(artist)

    # loop for adding to current playlist
    while loopAgain:
        # display current playlist
        print("Your playlist so far:")
        if not currentPlaylist:
            print("\tNothing in playlist")
            print("---------------")
        else:
            for pair in currentPlaylist:
                print("\t- %s by %s" % (pair[0], pair[1]))
            print("---------------")

        # display list of artists
        for artist in artistList:
            print("%d) %s" % (counter, artist))
            counter += 1
        counter = 0
        print("---------------")

        # ask user for artist
        while loopAgain:
            try:
                userInput = int(input("Select an artist from the list by entering its number: "))
                pickedArtist = artistList[userInput]
                loopAgain = False
            except:
                print("Please enter a valid number!")
                for artist in artistList:
                    print("%d) %s" % (counter, artist))
                    counter += 1
                counter = 0
                print("---------------")
        loopAgain = True

        # create a list of albums for the given artist
        for album in musicLibDictionary[pickedArtist]:
            albumList.append(album)

        # display list of albums by artist
        for album in albumList:
            print("%d) %s" % (counter, album))
            counter += 1
        counter = 0
        print("---------------")

        # ask user for album
        while loopAgain:
            try:
                userInput = int(input("Select an album from the list by entering its number: "))
                pickedAlbum = albumList[userInput]
                loopAgain = False
            except:
                print("Please enter a valid number!")
                for album in albumList:
                    print("%d) %s" % (counter, album))
                    counter += 1
                counter = 0
                print("---------------")
        loopAgain = True

        # add picked artist and album to current playlist
        currentPlaylist.append([pickedAlbum, pickedArtist])

        # ask user if want to continue
        while loopAgain:
            userInput = input("Would you like to continue building your playlist? (y/n) ")
            if userInput.lower() == "y":
                albumList = []
                break
            elif userInput.lower() == "n":
                for pair in currentPlaylist:
                    print("\t- %s by %s" % (pair[0], pair[1]))
                print("---------------")
                loopAgain = False
            else:
                print("Invalid input!")

main()