# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 9

import math


def main():
    print("This program prints the area of a triangle, given the length of")
    print("each side.")
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is: ", round(area, 2), "units squared.")


main()
