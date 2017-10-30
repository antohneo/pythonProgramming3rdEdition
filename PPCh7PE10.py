# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 10


def easterDate(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        if 22 + d + e - 7 <= 31:
            date = "Easter falls on March " + str((22 + d + e - 7))
        else:
            date = "Easter falls on April " + str((22 + d + e - 31 - 7))
        return date
    else:
        if 22 + d + e <= 31:
            date = "Easter falls on March " + str((22 + d + e))
        else:
            date = "Easter falls on April " + str((22 + d + e - 31))
        return date


def main():
    y = int(input("Enter the year: "))
    print(easterDate(y))


main()
