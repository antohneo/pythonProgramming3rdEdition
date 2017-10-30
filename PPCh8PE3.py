# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 3


def main():
    interest = float(input("Enter an interest rate [ie 2.5% -> (0.025)]: "))
    principal = 100
    futureVal = 0
    years = 0
    while futureVal <= 2*principal:
        years += 1
        if years == 1:
            futureVal = principal * (1+interest)
        else:
            futureVal = futureVal * (1+interest)
        print("After year {0} the value is: ${1:0.2f}".format(years, futureVal))


main()
