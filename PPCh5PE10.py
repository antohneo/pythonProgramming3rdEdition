# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 10


def main():
    # print intro
    print("This program calculates the average word length in a sentence.")
    # prompt for sentence
    sentence = str(input("Enter a sentence: "))
    # split phrase
    wordList = sentence.split()
    # loop words for total characters
    totalChars = 0
    for word in wordList:
        totalChars += len(word)
    # calculate total characters / number of words
    averageChars = totalChars / len(wordList)
    # print result
    print("The average length of words in the sentence:", sentence,
          "is {0:0.1f} characters".format(averageChars))


main()
