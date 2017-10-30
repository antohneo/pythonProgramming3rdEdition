# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 11


def main():
    print("This program calculates the future value")
    print("of a n-year investment.")

    principal = float(input("Enter the initial principal: "))
    dollars = principal // 1
    cents = round((principal - dollars) * 100 , 2)
    apr = float(input("Enter the annual interest rate: "))
    n = int(input("Enter the number of years invested: "))


    print("Year     Value  ")
    print("----------------")
    print("{0:^4} ${1:0.0f}.{2:2.0f}".format("0", dollars, cents))

    for i in range(1, n + 1):
        principal = principal * (1 + apr)
        dollars = principal // 1
        cents = round((principal - dollars) * 100 , 2)
        print("{0:^4} ${1:0.0f}.{2:0>2.0f}".format(i, dollars, cents))

    print("The value in 10 years is:", principal)


main()
