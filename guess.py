#This program chooses a random number based on the input bounds
#Written by Joseph Parampathu, 04/06/21

from GuessingGame import number  #number of guesses
from GuessingGame import bottom #lower bound for guess
from GuessingGame import top #upper bound for guess
import random #import random module
from GuessingGame import * #import data from GuessingGame.py
import sys # import sys

#Generate a new Guess
#Increase number count for incorrect guesses



while number < 4:
    number = number + 1

    if user_input == "correct":
        print("Yes! I won!")
        sys.exit()

    if user_input == "low":   #Set new lower bound based on input
        bottom = guessNumber;
    if user_input == "high":  #Set new upper bound based on input
        top = guessNumber;

    guessNumber = random.randint(bottom,top)

    print("I think the number is " + str(guessNumber) + ".")  #execute guess while incorrect
    user_input = raw_input("How\'d I do? Enter low, high, or correct:")
