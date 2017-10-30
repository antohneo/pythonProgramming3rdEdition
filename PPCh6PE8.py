# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Excercise 8

from math import sqrt

def nextGuess(guess, x):
    guess = (guess + x / guess) / 2
    return guess


def main():
    print("This program approximates a number's square root.")
    print("The first guess is n / 2, followed by (guess + n/guess) / 2.")
    n = int(input("Enter a number: "))
    nGuesses = int(input("Enter the number of guesses: "))
    for i in range(nGuesses):
        if i < 1:
            guess = n / 2
        else:
            guess = nextGuess(guess, n)
    print("The guess is: {0:0.2f}".format(guess))
    print("The actual root is: {0:0.2f}".format(sqrt(n)))
    print("The difference is: {0:0.2f}".format(sqrt(n) - guess))


main()
