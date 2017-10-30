# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 9


def main():
    # intro
    print("This program counts the nuber of words in a sentence.")
    # prompt for phrase
    sentence = str(input("Enter a sentence: "))
    # split phrase and count words
    wordCount = 0
    for word in sentence.split():
        wordCount += 1
    # print out the wordCount
    print("There are {0} words in the sentence".format(wordCount))


main()
