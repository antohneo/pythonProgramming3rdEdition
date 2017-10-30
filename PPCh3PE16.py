# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 16


def main():
    print("This program computers the nth Fibonacci number.")
    nTerms = int(input("Enter the number of terms: "))
    Fib = 0
    Fib_1 = 0
    Fib_2 = 0
    for i in range(nTerms):
        if i == 0:
            Fib = i
        if i == 1:
            Fib = i
            Fib_1, Fib_2 = Fib, Fib_1
        else:
            Fib = Fib_1 + Fib_2
            Fib_1, Fib_2 = Fib, Fib_1
        print("Fib:", Fib, "Fib_1:", Fib_1, "Fib_2:", Fib_2)
    # print(Fib)
    print("The", nTerms, "th Fibonacci number is", Fib)


main()
