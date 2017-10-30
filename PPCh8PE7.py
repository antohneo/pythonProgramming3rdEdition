# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 7

from math import sqrt


def isPrime(testValue):
    n = 2
    while (testValue % n != 0) and (n <= sqrt(testValue)):
        n += 1
    if testValue % n == 0:
        return False
    else:
        return True


def main():
    print("This program takes an even number and finds two prime numbers which")
    print("add up to the even number.")
    evenNumber = int(input("Enter an even number: "))
    if evenNumber % 2 != 0:
        print("The number is not even.")
    else:
        n = 2
        while (n <= evenNumber / 2) and not (isPrime(n) and isPrime(evenNumber - n)):
            n += 1
        print("{0} and {1} sum up to {2} and are prime.".format(n, evenNumber - n, evenNumber))


main()
