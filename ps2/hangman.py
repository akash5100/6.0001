# Problem Set 2, hangman.py
# Name: Akash
# Collaborators: Akash
# Time spent: 6 - 7

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
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    wordlist (list): list of words (strings)
    
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
    count = len(secret_word)
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                count-=1
    if count == 0:
      return True
    else:
      return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_of_secret_word = list(secret_word)
    guessed_word = ''
    for i in letters_of_secret_word:
        if i in letters_guessed:
            guessed_word += i 
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    string = 'abcdefghijklmnopqrstuvwxyz'
    for word in letters_guessed:
        if word in string:
            string = string.replace(word,'')
    return string
    
def unique_letters(secret_word):
  '''
  returns the number of unique letter in secret word
  '''
  letter = set(secret_word)
  i = len(letter)
  return i

def is_vowel(letter):
  '''
  return: 2 if letter guessed is vowel 
  return: 1 if letter guessed is Consonant
  '''
  vowel = ['a','e','i','o','u']
  if letter in vowel:
    return 2
  else:
    return 1

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
    i = len(secret_word)
    num_of_guess = 6
    warning = 3
    letters_guessed = []

    #start up 
    print(f'\nWelcome to the game Hangman!\nI am thinking of a word that is {i} letters long.\n') 
    print(f'You have {warning} warnings left.\n-------------')


    #promt user
    while num_of_guess != 0 and warning != 0:
      available_letters = get_available_letters(letters_guessed)
      
      print(f'You have {num_of_guess} guesses left.')
      print('available letters: ' + available_letters)

      #checking for lower case
      temp = input('Please guess a letter: ')
      letter = temp.lower()
      
      #checking for alphabet and single character
      if letter.isalpha() and len(letter) == 1:
        #checking if letter already in list
        if letter in letters_guessed:
          warning-=1
          print("\nOops! You've already guessed that letter")
          print(f"-------------\nYou have {warning} warnings left.")
          

        else:
          letters_guessed.append(letter)
          
          #searching letter in word
          if letter in secret_word:
            guessed_word = get_guessed_word(secret_word,letters_guessed)
            print('Good guess:' + guessed_word + "\n\n-------------\n")

            if is_word_guessed(secret_word,letters_guessed):
              print('\nCongratulations, you won!')
              score = num_of_guess * unique_letters(secret_word)
              print(f"Your total score for this game is: {score}")
              break
            

          else:
            guessed_word = get_guessed_word(secret_word,letters_guessed)
            print('Oops! That letter is not in my word: ' + guessed_word + "\n\n-------------\n")
            num_of_guess -= is_vowel(letters_guessed[-1])
    
      #warning if word is not alphabet
      else:
        warning-=1
        print(f"\n\n-------------\nYou have {warning} warnings left.")

    if (num_of_guess == 0):
      print(f"\nSorry, you ran out of guesses. The word was {secret_word}. ")
    elif (warning == 0):
      print(f"\nSorry, you ran out of warning. The word was {secret_word}. ")

        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #removing ' ' from my_word to compare length of my_Word and other_word
    for word in my_word:
      if word == '_':
        my_word = my_word.replace(word,'')
    
    if len(my_word) == len(other_word):
        my_list = list(my_word)

        for i in range(len(other_word)):
            if my_list[i] == other_word[i]:
                return True
            elif my_list[i] == ' ': #problem in this line
                return True
            else:
                return False
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
    my_list = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        my_list.append(word)
    if len(my_list) == 0:  
      print('no word found')

    print('matching words are: ')
    print(', '.join(my_list))


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

    i = len(secret_word)
    num_of_guess = 6
    warning = 3
    letters_guessed = []

    #start up 
    print(f'\nWelcome to the game Hangman!\nI am thinking of a word that is {i} letters long.\n') 
    print(f'You have {warning} warnings left.\n-------------')


    #promt user
    while num_of_guess != 0 and warning != 0:
      available_letters = get_available_letters(letters_guessed)
      
      print(f'You have {num_of_guess} guesses left.')
      print('available letters: ' + available_letters)

      #checking for lower case
      temp = input('Please guess a letter: ')
      letter = temp.lower()
      
      #checking for alphabet and single character
      if letter.isalpha() and len(letter) == 1:
        #checking if letter already in list
        if letter in letters_guessed:
          warning-=1
          print("\nOops! You've already guessed that letter")
          print(f"-------------\nYou have {warning} warnings left.")
          

        else:
          letters_guessed.append(letter)
          
          #searching letter in word
          if letter in secret_word:
            guessed_word = get_guessed_word(secret_word,letters_guessed)
            print('Good guess:' + guessed_word + "\n\n-------------\n")

            if is_word_guessed(secret_word,letters_guessed):
              print('\nCongratulations, you won!')
              score = num_of_guess * unique_letters(secret_word)
              print(f"Your total score for this game is: {score}")
              break
            

          else:
            guessed_word = get_guessed_word(secret_word,letters_guessed)
            print('Oops! That letter is not in my word: ' + guessed_word + "\n\n-------------\n")
            num_of_guess -= is_vowel(letters_guessed[-1])
        
      #if letter is * (user asking for hint)
      elif len(letter) == 1 and letter == '*':
        show_possible_matches(letter)  
    
      #warning if word is not alphabet
      else:
        warning-=1
        print(f"\n\n-------------\nYou have {warning} warnings left.")

    if (num_of_guess == 0):
      print(f"\nSorry, you ran out of guesses. The word was {secret_word}. ")
    elif (warning == 0):
      print(f"\nSorry, you ran out of warning. The word was {secret_word}. ")
  
    

# When you've completed your hangman_with_hint function, comment the two similar
# lines above twordlist = load_words()


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    '''secret_word = choose_word(wordlist)
    hangman(secret_word)'''

    ###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    secret_word = 'apple'
    hangman_with_hints(secret_word)
    