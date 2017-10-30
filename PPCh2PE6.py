# futval.py
#    A program to compute the value of an annual investment
#    carried n years into the future


def main():


    print("This program calculates the future value")
    print("of an investment for n-years.")

    investment = int(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))


    for i in range(years):
        investment = investment * (1 + apr)


    print("The value in", years, "years is:", investment)
    input("[ Press the <Enter> key to quit. ]")


main()