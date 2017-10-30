# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 17
import math


def main():
    print("This program approximates a number's square root.")
    print("The first guess is n / 2, followed by (guess + n/guess) / 2.")
    n = int(input("Enter a number: "))
    nGuesses = int(input("Enter the number of guesses: "))
    for i in range(nGuesses):
        if i < 1:
            guess = n / 2
        else:
            guess = (guess + n / guess) / 2
    print("The guess is:", guess)
    print("The actual root is:", round(math.sqrt(n), 2))
    print("The difference is:", round(math.sqrt(n) - guess, 2))


main()
