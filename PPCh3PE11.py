# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 11


def main():
    print("This program calculates the sum of the first n natural numbers.")
    n = int(input("Enter a positive integer: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("The sum of the first", n, "natural numbers is", total, ".")


main()
