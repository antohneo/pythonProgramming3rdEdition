# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 12


def main():
    print("Calculates the sum of the cubes of the first n natural numbers.")
    n = int(input("Enter a positive integer: "))
    total = 0
    for i in range(1, n + 1, 1):
        total += i**3
    print("The sum of cubes of the first", n, "natural numbers is", total, ".")


main()
