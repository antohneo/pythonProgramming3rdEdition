# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 10

import math


def main():
    print("This program calculates the length of a ladder needed to reach")
    print("a given height given the angle of the ladder.")
    height = float(input("Enter the desired height to reach: "))
    degrees = float(input("Enter the angle of the ladder in degrees: "))
    radians = math.pi / 180 * degrees
    length = height / math.sin(radians)
    print("You need a ladder of length", round(length, 0))
    print("to reach the height.")


main()
