

import random
from random import randint

print("Welcome to the number guessing game!")
'''
my_seed = input("Enter random seed: ")
random.seed(my_seed)

num = randint(1, 100)
'''
#Select a Random , Number and reset, Guess Counter



def guessing():
    guess = 0
    numGuess = 0
    my_seed = input("Enter random seed: ")
    random.seed(my_seed)
    num = randint(1, 100)
    while guess != num:
        guess = int(input('Please enter a guess: '))
        numGuess += 1
        if guess > num:
            print("Lower")
            print(" ")
        elif guess < num:
            print("Higher")
            print(" ")
    print('Congratulations. You guessed it!')
    print('It took you {} guesses.'.format(numGuess))
    print(" ")
    play_again(guess)

def play_again(guess):
    playAgain = input('Do you want to play again? (yes/no): ')
    if playAgain == "yes":
        guessing()
    elif playAgain == 'no':
        quit()

def quit():
    print('Thank you. Goodbye.')
            
guessing()   
    
    
    
#GEt a guess from user

#Upate guess counter

#compare guess


    
# Print "Higher"

# Print Lower 
    
#Print "Congrats!" and display Guess Counter

#ask if they want to play again

#Yes

#No

