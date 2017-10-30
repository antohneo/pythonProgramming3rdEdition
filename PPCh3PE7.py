# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 7


import math


def main():
    print("Program calculates the distance between 2 cartesian coordinates.")
    x1 = int(input("Enter X1: "))
    y1 = int(input("Enter Y1: "))
    x2 = int(input("Enter X2: "))
    y2 = int(input("Enter Y2: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("The slope of the line between the points is:", round(distance, 2))


main()
