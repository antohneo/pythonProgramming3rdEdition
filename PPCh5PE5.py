# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 5


def main():
    # print into
    print("This program calculcates the numeric value of a name where A=1 Z=26")
    # prompt for name
    word = str(input("Enter a name: "))
    # loop through characters and sum
    tot = 0
    for ch in word.lower():
        tot += ord(ch) - 96
    # print final result
    print("The sum of the name: {0} is equal to: {1}".format(word, tot))


main()
