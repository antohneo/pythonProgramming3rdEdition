# futval.py
#    A program to compute the value of an annual investment
#    carried n years into the future


def main():

    print("This program calculates the future value")
    print("of a yearly investment for n-years.")

    annualInvestment = int(input("Enter the annual principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))
    total = 0.00
    for i in range(years):
        total = (total + annualInvestment) * (1 + apr)

    print("The value in", years, "years is:", total)
    input("[ Press the <Enter> key to quit. ]")


main()