# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 10


def acronym(phrase):
    # split string
    words = phrase.split()
    # transverse list: get 1st letter and uppercase
    acronym = ""
    for word in words:
        acronym += word.upper()[0]
    return acronym


def main():
    # intro
    print("This program creates an acronym using the 1st letters of each word",
          "entered.")
    # get phrase
    phrase = str(input("Type in a phrase and hit <Enter>: "))

    # print acronym
    print("The acronym for '{0}' is '{1}'.".format(phrase, acronym(phrase)))


main()
