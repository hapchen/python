# -*- coding: utf-8 -*-
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/Haipei/Documents/Python/6.00.1x Files/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
    

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            result += 1
    return result == len(secretWord)
            


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    output = ''
    result = list(secretWord)
    for i in range(0,len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            result[i]='_ '
        output += result[i]
    return output


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    import string
    all = list(string.ascii_lowercase)
    for i in range(0,len(all)):
        if all[i] not in lettersGuessed:
            result += all[i]
    return result

# Problem set 3 answer
def hangman(secretWord):
    # secretWord: string, the secret word to guess.
    # Set up some empty variable for the function
    guesstime = 0 
    result = ''
    lettersGuessed = []
    # Set up the max guess times
    if len(secretWord) < 6:
        l = 8
    elif len(secretWord) <10:
        l = 9
    else:
        l = 10
    
    '''
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord)) + ' letters long.')
    
    '''
    * Ask the user to supply one guess per round.
    '''
    while guesstime < l:
        print('------------')
        print('You have '+str(l-guesstime) + ' guesses left.')
        
     	# Tell the user how many letters are available to guess
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters: '+availableLetters)
        
        # User to input the guessed letter
        guess = raw_input('Please guess a letter: ')
        guessInLowerCase = guess.lower()
        # Check the input to make sure it is ONE LETTER
        if len(guessInLowerCase) != 1 or guessInLowerCase not in 'abcdefghijklmnopqrstuvwxyz':
            print('Oops! You did not enter a letter')
            continue
        
        # Get the result of the guess 
        if guessInLowerCase in lettersGuessed:
            result = getGuessedWord(secretWord, lettersGuessed)
            print("Oops! You've already guessed that letter: "+ result)
            continue
            
        else:
            lettersGuessed += guessInLowerCase
            result = getGuessedWord(secretWord, lettersGuessed)
            if guessInLowerCase in secretWord:
                print('Good guess: ' + result) 
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print('------------')
                    print('Congratulations, you won!')
                    return 
                continue
            else:
                print('Oops! That letter is not in my word: ' + result)
                guesstime += 1  
                if guesstime == l:
                    print('-----------')
	            print('Sorry, you ran out of guesses. The word was else.')
	            return








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# print(secretWord)    ---- for testing
hangman(secretWord)
