# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 5


def main():
    print("This program calculates the cost of an order.")
    pounds = float(input("Enter the number of pounds of coffee ordered: "))
    coffee = pounds * 10.50
    cost = 0.86 * pounds + 1.50
    print("This order costs", round(cost, 2), "to ship. And")
    print(round(coffee, 2), "for coffee. Totalling:", round(coffee + cost, 2))


main()
