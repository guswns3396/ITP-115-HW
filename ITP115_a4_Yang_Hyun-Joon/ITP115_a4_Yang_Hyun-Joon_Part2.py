# Hyun-Joon Yang
# ITP 115, Fall 2018
# Assignment 4
# yanghyun@usc.edu


##############################################################################################
# PART 2: ENCRYPT / DECRYPT


def main():
    originalMessage = []
    encryptedMessage = []
    decryptedMessage = []
    shift = 0

    # get user message to encrypt
    userInput = input("Enter a message to encrypt: ")
    originalMessage = list(userInput)

    # get shift factor
    shift = int(input("Enter a number to shift by: "))

    # get the encrypted message
    encryptedMessage = encrypt(originalMessage, shift)

    print("".join(encryptedMessage))

    # get user message to decrypt
    userInput = input("Enter a message to decrypt: ")
    encryptedMessage = list(userInput)

    # get shift factor
    shift = int(input("Enter the number used to shift: "))

    # get decrypted message
    decryptedMessage = decrypt(encryptedMessage, shift)

    print("".join(decryptedMessage))
#-------------------------------------------------------------------------------------------------

# function to encrypt message
# gets original message and shift factor as input
# returns a encrypted message as a list
def encrypt(arg_orginalMessage, arg_shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list = []

    # look at each character of original message and add to the list as encrypted
    for character in arg_orginalMessage:
        # in case of capitalization
        isCapitalized = False
        if character.capitalize() == character:
            isCapitalized = True
        # turn it into lowercase for simplicity
        character = character.lower()
        # if character an alphabet then shift
        if character in alphabet:
            alphabetIndex = alphabet.find(character)
            # if shifting requires starting over from the alphabet
            if alphabetIndex + arg_shift >= len(alphabet):
                character = alphabet[(alphabetIndex + arg_shift) % 26]
                if isCapitalized:
                    character = character.capitalize()
                list.append(character)
            else:
                character = alphabet[alphabetIndex + arg_shift]
                if isCapitalized:
                    character = character.capitalize()
                list.append(character)
        # if character not an alphabet then just add to list
        else:
            list.append(character)


    return list
#-------------------------------------------------------------------------------------------------

# function to decrypt message
# gets the encrypted message and shift factor as input
# returns decrypted message as a list
def decrypt(arg_encryptedMessage, arg_shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list = []

    # look at each character of original message and add to the list as encrypted
    for character in arg_encryptedMessage:
        # in case of capitalization
        isCapitalized = False
        if character.capitalize() == character:
            isCapitalized = True
        # turn it into lowercase for simplicity
        character = character.lower()
        # if character an alphabet then shift
        if character in alphabet:
            alphabetIndex = alphabet.find(character)
            # if shifting requires starting over from the alphabet
            if alphabetIndex - arg_shift < 0:
                character = alphabet[alphabetIndex - (arg_shift % 26)]
                if isCapitalized:
                    character = character.capitalize()
                list.append(character)
            else:
                character = alphabet[alphabetIndex - arg_shift]
                if isCapitalized:
                    character = character.capitalize()
                list.append(character)
        # if character not an alphabet then just add to list
        else:
            list.append(character)


    return list
#-------------------------------------------------------------------------------------------------

# run program
main()