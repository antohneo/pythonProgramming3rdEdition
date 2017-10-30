# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 5
# Programming Excercise 1


def main():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[month - 1]

    print("The date is {1:02}/{0:02}/{2} or".format(day, month, year),
           monthStr, "{0:02}, {2}".format(day, month, year))


main()
