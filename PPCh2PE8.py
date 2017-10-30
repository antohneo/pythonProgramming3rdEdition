# futval.py
#    A program to compute the value of an investment
#    carried n years into the future


def main():

    print("This program calculates the future value")
    print("of an investment n-years into the future.")

    investment = int(input("Enter the annual principal: "))
    rate = float(input("Enter the nominal interest rate: "))
    periodsPerYear = int(input("Enter the number of annual compounding periods: "))
    years = int(input("Enter the number of years: "))
    for i in range(years * periodsPerYear):
        investment = investment * (1 + rate / periodsPerYear)

    print("The value in", years, "years is:", investment)
    input("[ Press the <Enter> key to quit. ]")

main()