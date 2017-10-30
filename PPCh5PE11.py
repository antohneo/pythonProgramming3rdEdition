# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 11


def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 & 1: "))
    y = float(input("Enter another number between 0 & 1: "))
    n = int(input("Enter the number of iterations to do: "))
    print("{0} {1:^11} {2:^11}".format("index", x, y))
    print("----------------------------")
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("{0:^4} {1:^12.6f} {2:^12.6f}".format(i, x, y))


main()
