# pizzacost.py
# calculates the cost per sq. inch of circular pizza
# python3

from math import pi


def main():
    # inputs
    print("This program calculates the cost per sq. inch of a circular pizza.")
    d = int(input("Enter the diameter of the pizza in inches: "))
    p = float(input("Enter the price of the pizza: "))

    # calculate
    area = calcArea(d)
    pricePerSqInc = calcPerSqInch(area, p)


    print("For a {0}\" pizza priced at ${1:0.2f} the price per square inch is {2:0.2f}".format(
        d, p, pricePerSqInc))


def calcArea(diameter):
    area = pi * ((diameter / 2) ** 2)
    return area


def calcPerSqInch(area, price):
    perSquareInch = price / area
    return perSquareInch


main()
