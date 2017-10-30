# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 8


def main():
    print("This program finds the greatest common divisor using the Euclidean algorithm.")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    n, m = a, b
    while m != 0:
        n, m = m, n % m
    print("The greatest common divisor of {0} and {1} is: {2}.".format(a, b, n))


main()
