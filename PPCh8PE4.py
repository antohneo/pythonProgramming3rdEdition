# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 4


def syracuseFunction(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def main():
    startValue = int(input("Enter a natural number > 0 (i.e. 32,034): "))
    while startValue != 1:
        startValue = syracuseFunction(startValue)
        print("Current value is: {0:0.0f}".format(startValue))


main()
