# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 4


def main():
    # intro
    print("This program creates an acronym using the 1st letters of each word",
          "entered.")
    # get phrase
    phrase = str(input("Type in a phrase and hit <Enter>: "))
    # split string
    words = phrase.split()
    # transverse list: get 1st letter and uppercase
    acronym = ""
    for word in words:
        acronym += word.upper()[0]
    # print acronym
    print("The acronym for:", phrase, "is:", acronym + ".")


main()
