#hangman_final
#we will first take input from user1. user 1 will give the input for the word to be guesses
#user 2 will guess the letters in the secret word.
#user2 will have only 7 wrong guesses.
#alphabet limit for user 1 will be 6
#len(string)=6
#constraints: no numbers or special characters only alphabets and the user2 can only guess one letter at a time.

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import getpass
def pattern(n): #this funtion will be used to print the display of hangman corresponding to the number of wrong guesses the user2 has made.
    if n==0:
        print('''
    +---+
    |   |
        |
        |
        |
        |
==========''')

    elif n==1:
        print('''
    +---+
    |   |
    O   |
        |
        |
        |
==========''')

    elif n==2:
        print('''
    +---+
    |   |
    O   |
    |   |
        |
        |
==========''')

    elif n==3:
        print('''
    +---+
    |   |
    O   |
   /|   |
        |
        |''')

    elif n==4:
        print('''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
==========''')

    elif n==5:
        print('''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
==========''')

    elif n==6:
        print('''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
==========''')
    elif n==7:
        print('''
    +---+
    |   |
    O   |
---------
   /|\  |
   / \  |
        |
==========''')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

global secret_word

def secret_check(secret_word):
    secret_check.secret_word = secret_word
    for char in secret_word:
        if char.isalpha():
            if len(secret_word)!=6:
                print("Secret word should be 6 characters long.")
                secret_check.secret_word=input("Shhhhh...Please type in the secret word: ")
                break
    
        else:
            print("INPUTS MUST ONLY COMPRISE OF ALPHABETS.")
            secret_check.secret_word=input("Shhhhh...Please type in the secret word: ")
            break

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
        
def guess_check(secret_word):
    word_completion = "_" * len(secret_word)
    guessed = False
    guessed_letters = []
    n = 0
    print("Let's play Hangman")
    print(pattern(n))
    print(word_completion)
    print("\n")
    while not guessed and n < 7:
        guess = input("What's your guess?: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already tried "", guess, "" ! Try something else :)")
            elif guess not in secret_word:
                print("Try Again! "",guess, "" isn't in the word :(")
                n += 1
                guessed_letters.append(guess)
            else:
                print("You're correct! "", guess, "" is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(secret_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) != 1 and guess.isalpha():
            print("Oopsies...You can only guess 1 alphabet at a time.")
        else:
            print("looks like your input is invalid :o")
        print(pattern(n))
        print(word_completion)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word!")
        x = input('Do you want to play again?')
        if x=='YES':
            guess_check(secret_word)
        elif x=='NO':
            print('Good bye.')

        print('')
    else:
        print("Sorry, you ran out of tries. The word was " + secret_word + ". Maybe next time!")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Welcome to Hangman: Re-imagined!!")
print("The rules for this game are as follows:")
print("1- you can only guess one alphabet at a time", "2- The secret word can only have alphabets and should be 6 characters long", sep='\n')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

secret_word = getpass.getpass(prompt='Shhhhh...Please type in the secret word: ')
print('')
print('')
secret_word=secret_word.upper()
secret_check(secret_word)
secret_word = secret_check.secret_word.upper()
guess_check(secret_word)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------