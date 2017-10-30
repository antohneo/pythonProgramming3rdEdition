# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 6

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
    print("This program returns prime numbers between numbers entered.")
    start = int(input("Enter a starting point (n > 2): "))
    end = int(input("Enter an ending point: "))
    n = start
    while n < (end + 1):
        if isPrime(n):
            print("{0} is prime.".format(n))
        n += 1


main()
