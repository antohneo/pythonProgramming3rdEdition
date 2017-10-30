# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 4


def main():
    print("This program classifies students based on the number of credits earned.")
    credits = int(input("Enter the number of credits earned: [0-100] "))
    if credits < 7:
        year = "Freshman"
    elif credits < 16:
        year = "Sophomore"
    elif credits < 26:
        year = "Junior"
    else:
        year = "Senior"
    print("{0} credits is a {1} student.".format(credits, year))


main()
