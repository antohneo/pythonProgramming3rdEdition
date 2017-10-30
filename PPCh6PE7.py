# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 7


def fib(n):
    Fib = 0
    Fib_1 = 0
    Fib_2 = 0
    for i in range(n):
        if i == 0:
            Fib = i
        if i == 1:
            Fib = i
            Fib_1, Fib_2 = Fib, Fib_1
        else:
            Fib = Fib_1 + Fib_2
            Fib_1, Fib_2 = Fib, Fib_1
    return Fib


def main():
    print("This program computers the nth Fibonacci number.")
    nTerms = int(input("Enter the number of terms: "))

    # calculate term
    nthFib = fib(nTerms)

    # print(Fib)
    print("The {0}th Fibonacci number is {1}.".format(nTerms, nthFib))


main()
