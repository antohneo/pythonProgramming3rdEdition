# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 6


def main():
    print("This program calculates the slope between 2 cartesian coordinates.")
    x1 = int(input("Enter X1: "))
    y1 = int(input("Enter Y1: "))
    x2 = int(input("Enter X2: "))
    y2 = int(input("Enter Y2: "))
    slope = (y2 - y1) / (x2 - x1)

    print("The slope of the line between the points is:", round(slope, 2))


main()
