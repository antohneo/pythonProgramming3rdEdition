# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 5

from math import sqrt


def main():
    print("This program tests if a number (n > 2) is prime.")
    testPrime = int(input("Enter a positive whole number greater than 2: "))
    n = 2
    while (testPrime % n != 0) and (n <= sqrt(testPrime)):
        n += 1
    if testPrime % n == 0:
        print("{0} is evenly divided by {1}.".format(testPrime, n))
    else:
        print("{0} is prime.".format(testPrime))


main()
