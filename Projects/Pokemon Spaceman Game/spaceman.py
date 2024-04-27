'''
Evangeline Kim
Sept. 29th, 2023
---Note: All possible words to guess will be from the first twenty Gen 1 Pokémon---
'''

#Import necessary libraries
import random

#Global word list
WORD_LIST = ['BULBASAUR', 'IVYSAUR', 'VENASAUR', 'CHARMANDER', 
             'CHARMELEON', 'CHARIZARD', 'SQUIRTLE', 'WARTORTLE', 
             'BLASTOISE', 'CATERPIE', 'METAPOD', 'BUTTERFREE', 
             'WEEDLE', 'KAKUNA', 'BEEDRILL', 'PIDGEY', 
             'PIDGEOTTO', 'PIDGEOT', 'RATTATA', 'RATICATE']


def pick_random_word():
    '''Function pick_random_word() will choose a random word from a list of words, and return it.
    Parameters: None
    Returns: A random word from the list (WORD_LIST)
    '''
    return random.choice(WORD_LIST)


def create_hidden_word(rand_word):
    '''Function create_hidden_word() will create an obfuscated version of the random word.
    Parameters: The random word (rand_word)
    Returns: An obfuscated version of the word (ie 'VAN' would return '***')
    '''
    hidden_word = '*' * len(rand_word)
    return hidden_word


def word_found(rand_word, hidden_word):
    '''Function word_found() will detect whether or not the random word has been uncovered.
    Parameters: the random word (rand_word) and the new hidden word that you guessed up to.
    Returns: True if the hidden word has all been revealed, False otherwise
    '''
    if hidden_word == rand_word:
        return True
    else:
        return False


def replace_character(rand_word, hidden_word):
    '''Function replace_character() will replace all the correct guesses within hidden_word with the right letters.
    Stops once the hidden_word is fully guessed, or if you use up all chances.
    Parameters: the random word (rand_word), and the hidden word so far (hidden_word).
    Returns: the new hidden_word
    '''
    used_guesses = []
    chances = 6
    while chances > 0:
        user_guess = input("\nPlease make a guess!\n>>> ").upper()

        #Make sure all inputs are a single letter. Otherwise, prompt to try again.
        if len(user_guess) == 1 and user_guess.isalpha():
            
            #Has the guess already been used?
            if user_guess in used_guesses:
                print("\nYou've already guessed that letter!")
            elif user_guess not in used_guesses:
                used_guesses.append(user_guess)
                chances -= 1

                #Is the guess within the word?
                if user_guess in rand_word:
                    print("\nNice guess! That letter is in the word") 
                    chances += 1                   
                    #I got help through a youtube video/generating tests for this particular 'for' loop.
                    new_hidden_word = ''      
                    for letter in range(len(rand_word)):
                        if user_guess == rand_word[letter]:
                            new_hidden_word += user_guess
                        else:
                            new_hidden_word += hidden_word[letter]
                    hidden_word = new_hidden_word
                elif user_guess not in rand_word:
                    print("\nToo bad! That letter is not in the word.")
        elif len(user_guess) > 1 and user_guess.upper() == rand_word:
            hidden_word = rand_word
            break
        elif len(user_guess) > 1 and user_guess.upper() != rand_word and user_guess.upper() in WORD_LIST:
            print("\nThat was not the word!")
            chances -= 1
        else:
            print("\nInvalid input.")
        
        #break out of loop if the word is guessed early
        if word_found(rand_word, hidden_word) == True:
            break
        
        #Update user of status every time
        print("LETTERS GUESSED SO FAR: ", used_guesses)
        print("YOUR WORD SO FAR: ", hidden_word)
        print("ATTEMPTS LEFTOVER: ", (chances))
    return hidden_word


def main():
    '''Place where the spaceman game actually takes place.
    Calls back previously made functions.
    '''
    #Welcoming Statements
    print("\n|---WELCOME TO THE SPACEMAN GAME!---|\n")
    print("THE GOAL IS TO GUESS A 5-15 LETTER WORD WITH LESS THAN 6 WRONG GUESSES.")
    print("YOU MAY ALSO GUESS THE WORD IF YOU THINK YOU KNOW IT BEFOREHAND.")
    print("GUESS WELL OR ELSE THE ALIENS WIN!")
    
    #Variables
    rand_word = pick_random_word()
    hidden_word = create_hidden_word(rand_word)
    print("\nHere is your word: ", hidden_word)
    new_hidden_word = replace_character(rand_word, hidden_word)

    #Conditonal to generate game completion    
    if word_found(rand_word, new_hidden_word) == True:
        print("\nYOU WIN! YOU MAY STAY ON EARTH.")
        print("You guessed the word", rand_word, "within 6 guesses!")
    elif word_found(rand_word, new_hidden_word) == False:
        print("\nYOU LOSE! THE ALIENS HAVE WON. MUAHAHAHAH")
        print("It looke like you couldn't guess the word within 6 guesses.")
        print("The word you were trying to guess was", rand_word)
    print("\n\n|---THANKS FOR PLAYING THE SPACEMAN GAME!---|\n\n")
if __name__ == "__main__":
    main()
