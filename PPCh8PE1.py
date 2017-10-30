# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 1


def main():
    print("This program computes the N-th Fibonacci number, N is specified.")
    n = int(input("Enter the N-th Fibonacci number to calculate [1-999,999]: "))

    i = 0
    fib = 0
    fib_n1 = 0
    fib_n2 = 0
    while (i != n):
        if i == 0:
            fib = 1
        else:
            fib = fib_n1 + fib_n2
        fib_n1, fib_n2 = fib, fib_n1
        i += 1
        print("The {0} Fibonacci is: {1}".format(i, fib))


main()
