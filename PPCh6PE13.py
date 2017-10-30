# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 13


def toNumbers(strList):
    # nums is a list of strings, function modifies list by converting to floats
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def main():
    # Get list of numbers
    strings = str(input("Enter a list of numbers separated by commas:"))
    myList = strings.split(",")
    # square list
    toNumbers(myList)
    # check transformation
    print(myList)


main()
