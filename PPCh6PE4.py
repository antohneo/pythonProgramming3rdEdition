# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 6
# Programming Excercise 4


def main():
    # intro
    print("This program calculates the sum of the first n natural numbers",
        "and the sum of the cubes of the first n natural numbers." )
    # prompt for number
    n = int(input("Enter a whole number: "))
    # print result
    print("The sum of the first {0} natural numbers is: {1}".format(
        n, sumN(n)))
    print("The sum of the cubes of the first {0} natural numbers".format(n),
        "is: {0}.".format(sumNCubes(n)))


def sumN(n):
    # returns the sum of the first n natural numbers
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sumNCubes(n):
    # returns the sum of the cubes of the first n natural numbers
    total = 0
    for i in range(1, n + 1):
        total += n ** 3
    return total


main()
