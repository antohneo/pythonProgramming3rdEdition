# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 3
# Excercise 8


def main():
    print("This program calculates the Gregorian epact.")
    year = int(input("Enter 4 digit year: "))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    print("The epact is:", epact)


main()
