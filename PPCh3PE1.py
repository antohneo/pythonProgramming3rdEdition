# sphere.py
# python3
# calculates volume and surface area of a sphere given radius

import math


def main():
    print("Program calculates the vol. & surface area of a sphere given the radius.")
    radius = float(input("Enter the radius of a sphere: "))
    volume = 4 / 3 * math.pi * radius ** 3
    surfaceArea = 4 * math.pi * radius ** 2

    print("The radius volume is:", round(volume, 2), "and the surface area is:", round(surfaceArea, 1))


main()
