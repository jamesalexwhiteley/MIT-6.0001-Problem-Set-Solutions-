# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.//
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)//
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return(set(secret_word) & set(letters_guessed) == set(secret_word))

secret_word = choose_word(wordlist)

# print(is_word_guessed(secret_word, letters_guessed))     

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_wordlist = list(secret_word)
    letters_guessedlist = list(letters_guessed)
    emptylist = ['_']*len(secret_word)
    counter = -1

    for i in secret_wordlist:
        counter += 1 
        if i in letters_guessedlist:
            emptylist[counter] = i 
    return ''.join(emptylist)
            
# print(secret_word)
# print(get_guessed_word(secret_word, letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alph = 'abcdefghijklmnopqrstuvwxyz'
    alphlist = list(alph)
    letters_guessedlist = list(letters_guessed)

    for i in letters_guessedlist:
        if i in alphlist:
            alphlist.remove(i)

    return 'Available_letters: '+''.join(alphlist)

# print(get_available_letters(letters_guessed))     


def check_common(secret_word, current_guess):

    a = set(secret_word)
    b = set(current_guess)
    if (a & b):
        return True
    else:
        return False

# check_common(secret_word, letters_guessed)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guesses = 6 
    print('Word contains', len(secret_word),'letters')
    letters_guessed = []

    while guesses > 0:
        print('You have', guesses,'guesses left')
        print(get_available_letters(letters_guessed))
        print(get_guessed_word(secret_word, letters_guessed)) 

        current_guess = input('Guess a letter: ')
        letters_guessed.append(current_guess)

        if is_word_guessed(secret_word, current_guess):
            print('You win!')
            break

        if check_common(secret_word, current_guess):
            pass
        else: 
            guesses -= 1
              
        print()

    print('You lose!')

# hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# 
# -----------------------------------

# other_word = 'hippy'
# my_word = 'hippy'

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    special = '_'
    if len(other_word) == len(my_word):
        for i in other_word:
            if my_word[count] == i:
                pass
            elif my_word[count] == special:
                pass 
            else:
                return False
                break   
            count += 1
        return True     
    else: 
        return False 


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matchlist = []
    wordlist = load_words()
    count = 0
    other_word = secret_word

    for i in wordlist: 
        if match_with_gaps(my_word, i) == True: 
            matchlist.append(i)      
        count += 1 
    return print(matchlist) 

# print(show_possible_matches('happy'))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6 
    print('Word contains', len(secret_word),'letters')
    letters_guessed = []
    special_counter = 3

    while guesses > 0:
        print('You have', guesses,'guesses left')
        print(get_available_letters(letters_guessed))
        print(get_guessed_word(secret_word, letters_guessed)) 

        current_guess = input('Guess a letter: ')
        letters_guessed.append(current_guess)

        special_guess = '*'
        if special_counter > 0: 
            if current_guess == special_guess:
                my_word = get_guessed_word(secret_word, letters_guessed)
                print(show_possible_matches(my_word))
                special_counter -= 1 

        if is_word_guessed(secret_word, letters_guessed):
            print('You win!')
            break

        if check_common(secret_word, current_guess):
            pass

        else: 
            guesses -= 1
              
        print()
    print('you lose!', 'The word was:', secret_word)

    # print('You lose!')

# hangman_with_hints(secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
