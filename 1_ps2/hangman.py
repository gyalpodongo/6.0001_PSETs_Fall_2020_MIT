# Problem Set 2, hangman.py
# Name: Gyalpo M Dongo Aguirre
# Collaborators:
# Time spent: 3:30

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
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
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if secret_word == "":
        x =  True
    else: 
        for i in secret_word:
            if i in letters_guessed:
                x = True
            else:
                x = False
                break
            #code will break once a letter of secret_word is not found in 
            #letters_guessed meaning that the player hasn't won yet
    return x
    
def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = ""
    for i in secret_word:
        #use of for loop with secret_word instead of letters_guessed because
        #the order of the words in word_progress has to match the one of
        #secret_word
        if i in letters_guessed:
            word_progress += i
        else:
            word_progress += "*"
    return word_progress
            
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    available_letters = ""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            #as string is inmutable, it is easier to create a new string
            #with the available letters
            available_letters += i
    return available_letters
    
def get_revealed_letter(secret_word,available_letters):
    #new helper function created for when the player is receiving help
    choose_from = ""
    for i in available_letters:
        if i in secret_word:
            choose_from += i
    new = random.randint(0, len(choose_from)-1)
    #use of -1 due to index, then new is a random index of the letters that
    #are part of the secret_word but have not been chosen yet
    
    revealed_letter = choose_from[new]
    return revealed_letter
    

def hangman(secret_word, with_help):
    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '^'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol ^, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    num_guess = 10
    letters_guessed = []
    word_progress = get_word_progress(secret_word,letters_guessed)
    available_letters = get_available_letters(letters_guessed)
    vowels = "aeiou"
    print("""Welcome to Hangman!
I am thinking of a word that is""", len(secret_word), "letters long")
    print("--------------")
    while num_guess > 0 or word_progress != secret_word:
        if num_guess == 1:
            print("You have 1 guess left")
        else:
            print("You have",num_guess,"guesses left")
        print("Available letters:",available_letters)
        guess = str(input("Please guess a letter: "))
        if guess.isalpha() == True:
            #making sure the guess is either a word or a letter
            if len(guess) >1:
                #if len(guess) is greater than oone, it is a word then
                print("""Oops! That is not a valid letter. Please input a letter from
the alphabet:""",word_progress)
                print("--------------")
            else:
                if guess.lower() in secret_word:
                    if guess.lower() in letters_guessed:
                        available_letters = get_available_letters(letters_guessed)
                        word_progress = get_word_progress(secret_word,letters_guessed)
                        print("Oops! You've already guessed that letter:",word_progress)
                        print("--------------")
                    else:
                        letters_guessed.append(guess.lower())
                        available_letters = get_available_letters(letters_guessed)
                        word_progress = get_word_progress(secret_word,letters_guessed)
                        print("Good guess:",word_progress)
                        print("--------------")
                else:
                    if guess.lower() in letters_guessed:
                        available_letters = get_available_letters(letters_guessed)
                        word_progress = get_word_progress(secret_word,letters_guessed)
                        print("Oops! You've already guessed that letter:",word_progress)
                        print("--------------")
                    else:
                        if guess.lower() in vowels:
                            letters_guessed.append(guess.lower())
                            available_letters = get_available_letters(letters_guessed)
                            word_progress = get_word_progress(secret_word,letters_guessed)
                            print("Oops! That letter is not in my word:",word_progress)
                            print("--------------")
                            if num_guess >= 2:
                                num_guess -= 2
                            else:
                                break
                            
                        else:
                            num_guess -= 1
                            letters_guessed.append(guess.lower())
                            available_letters = get_available_letters(letters_guessed)
                            word_progress = get_word_progress(secret_word,letters_guessed)
                            print("Oops! That letter is not in my word:",word_progress)
                            print("--------------")             
        else:
            if with_help == True:
                if guess == "^":
                    if num_guess > 3:
                        revealed_letter = get_revealed_letter(secret_word,available_letters)
                        letters_guessed.append(revealed_letter)
                        available_letters = get_available_letters(letters_guessed)
                        word_progress = get_word_progress(secret_word,letters_guessed)
                        print("Letter revealed:",revealed_letter)
                        print(word_progress)
                        print("--------------")
                        num_guess -= 3
                    else:
                        print("Oops! Not enough guesses left:",word_progress)
                        print("--------------")
                else:
                    print("""Oops! That is not a valid letter. Please input a letter from
the alphabet:""",word_progress)
                    print("--------------")
            else:
                print("""Oops! That is not a valid letter. Please input a letter from
the alphabet:""",word_progress)
                print("--------------")
        if num_guess == 0:
            break
        elif secret_word == word_progress:
            break
        
    unique_secret_word = set()
    #use of set to get rid of repeated letters
    for i in secret_word:
        unique_secret_word.add(i)
    total_score =  2*len(unique_secret_word)*num_guess + 3*len(secret_word)
    if has_player_won(secret_word,letters_guessed) == True:
        print("Congratulations, you won!")
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was",secret_word)
        
            
        
        
        
                
                    
                    
                    

                
                
        
                
                
                
                
                
            
                



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
        #secret_word = choose_word(wordlist)
        secret_word = "stiro"
        with_help = True
        hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "^" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    