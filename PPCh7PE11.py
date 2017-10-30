# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 11


def main():
    year = int(input("Enter a year: "))
    century = year // 100
    if year % 4 == 0:
        if century % 4 == 0:
            print("{0} is a leap year.".format(year))
        else:
            print("{0} is not a leap year.".format(year))
    else:
        print("{0} is not a leap year.".format(year))  


main()
