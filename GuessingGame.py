#This program tries to guess the player's number from 1-100
#It makes successive guesses after asking
#input from the player regarding the previous guess
#Written by Joseph Parampathu, 04/06/21


#Guess a number
number = 0  #number of guesses
bottom = 1 #lower bound for guess
top = 100  #upper bound for guess
mainNumber = 0 #number of times GuessingGame.py has executed
printNumber = 0 #number of times losing statement has posted
import random #import random module
from guess import * #import guess.py module

    #Generate a new Guess

if mainNumber == 0:
    print("Time to play Guessing Game!")
    guessNumber = random.randint(bottom,top)
    print("I think the number is " + str(guessNumber) + ".")
    user_input = raw_input("How\'d I do? Enter low, high, or correct:")
    mainNumber = mainNumber + 1

if user_input != "correct" and number <= 5:
    execfile('guess.py')

if printNumber == 0 and user_input!= "correct":
    printNumber = printNumber + 1
    print("Darn, I lose!")
