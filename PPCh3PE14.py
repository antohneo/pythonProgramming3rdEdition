# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 14


def main():
    print("Calculates the average of a series numbers entered.")
    n = int(input("How many numbers will you enter: "))
    total = 0
    for i in range(n):
        value = float(input("Enter a number: "))
        total += value
    average = total / n
    print("The average of the numbers entered is", average)


main()
