# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 6
# Programming Excercise 3

from math import pi


def main():
    print("Calculates the vol. & surface area of a sphere given the radius.")
    radius = float(input("Enter the radius of a sphere: "))

    print("The volume is: {0:0.2f} and the surface area is: {1:0.2f}.".format(
        sphereVolume(radius), sphereArea(radius)))


def sphereArea(radius):
    surfaceArea = 4 * pi * radius ** 2
    return surfaceArea


def sphereVolume(radius):
    volume = 4 / 3 * pi * radius ** 3
    return volume


main()
