'''
Evangeline Kim
Sept. 22nd, 2023
CS5001 Mini Project
Guess My Number Program: Play a number guessing game with the program!
Whether your number of guesses is efficient is based on the binary search method.
'''

#Import necessary libraries
import sys
import random
import math


def high_or_low(my_num, num):
    '''Function name high_or_low(my_num, num) where my_num is the user's guess and num is the selected number
    Parameters: Two integers, my_num and num
    Returns: Whether user's number is too high or too low. Prints to user.
    '''
    #conditional statement
    if my_num > num:
        print("\nYour guess is too high.")
    else:
        print("\nYour guess is too low.")


def efficiency(my_num, num, max_range):
    '''Function name efficiency() will keep count of how many guesses you take to succeed and tell you if your guessing was efficient.
    Efficiency is based on the binary search method.
    Parameters: 3 integers my_num, num, and the maximum range (max_range) of the selected number (num).
    Returns: A count of how many times you had to guess until successful. Whether or not your were an efficient guesser.
    '''    
    #count starts at 2 b/c you take the  guesses in the main() and high_low() functions into account.
    count = 2
    
    #try/except block to account for multiple user input errors for my_num.
    while True:   
        try:
            my_num = int(input("Please try again:\n>>> "))
        except ValueError:
            print("\nInvalid input. Integer required.")
            continue
        else:
            break
    
    #loop condition
    while my_num != num:                
        if my_num > num:
            count += 1
            #try/except block to account for multiple user input errors for my_num.
            while True:
                try:
                    my_num = int(input("\nToo high! Please try again!:\n>>> "))
                except ValueError:
                    print("\nInvalid input. Integer required.")
                    continue
                else:
                    break
        elif my_num < num:
            count += 1
            #try/except block to account for multiple user input errors for my_num.            
            while True:
                try:
                    my_num = int(input("\nToo low! Please try again:\n>>> "))
                except ValueError:
                    print("\nInvalid input. Integer required.")
                    continue
                else:
                    break
        elif my_num == num:
            count += 1
            #try/except block to account for multiple user input errors for my_num.            
            while True:
                try:
                    my_num = int(input("\nThat's the same number! Please try again:\n>>> "))
                except ValueError:
                    print("\nInvalid input. Integer required.")
                    continue
                else:
                    break
    print("\nCongrats! You guessed the number!")
    
    #calculating efficiency through a binary search method.
    if count <= math.ceil(math.log2(max_range)):
        print("\nIt took you", count, "tries to succeed.","\nThe goal was to guess within", math.ceil(math.log2(max_range)), "tries to succeed.\nYou were efficient!")
    else:
        print("\nIt took you", count, "tries to succeed.","\nThe goal was to guess within", math.ceil(math.log2(max_range)), "tries to succeed.\nYou were not efficient.")


def main():
    '''The main() will ask for a maximum range to decide where selected number (num) will be chosen from.
    The main() will ask for a first number to guess (accounting for input errors)
    It will ask which function method to use (hot_cold or efficiency) and run the chosen method, calling back the created functions.
    Once the number guessed is the same as the selected number (num), the user wins.
    '''        
    #defining maximum range from which selected number (num) is chosen. Account for value error.
    try:
        if len(sys.argv) > 1:
            num = random.randint(1, int(sys.argv[1]))
            max_range = int(sys.argv[1])
            print("\nThe range is from 1 to", int(sys.argv[1]))
        elif not len(sys.argv) > 1:
            num = random.randint(1, 100)
            max_range = 100
            print("\nThe range is from 1 to 100.")
    except ValueError:
        print("\nThere as a value error. Please re-run code with integers.")

    #ask for a number to assign to my_num variable. Account for incorrect user input (like inputting a string instead of an integer)
    while True:
        try:
            my_num = int(input("Please guess a number:\n>>> "))
        except ValueError:
            print("\nInvalid input. Please enter an integer.")
            continue
        else:
            break

    if my_num == num:
        print("\nToday's your lucky day!! You guessed the number on the first try! Very efficient!")
    else:    
        high_or_low(my_num, num)
        efficiency(my_num, num, max_range)

if __name__ == "__main__":
    main()