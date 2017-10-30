# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 15

import math


def main():
    print("This program evaluates first n-terms of pi to compare them to pi.")
    print("Using the equation: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...")
    nTerms = int(input("Enter the number of terms: "))
    approximation = 0
    oddOrEven = 0
    for i in range(1, nTerms * 2, 2):
        approximation += (4 / i) * ((-1)**oddOrEven)
        oddOrEven += 1
        print(approximation)
    print("Pi - approximation is:", math.pi - approximation)


main()
