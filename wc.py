# aaa
# python3

# wc.py
#   Calculates the number of characters, number of words, average wordlength,
#   and the number of lines in a file.

from tkinter.filedialog import askopenfilename


def main():
    print("This program calculates the number of characters, number of words,",
          " average wordlength, and the number of lines in a file.")

    # get filenames
    infileName = askopenfilename()

    # open the files & create objects
    infile = open(infileName, "r")

    # create counts
    characters = 0
    words = 0
    lines = 0

    # process each line of the input file
    for line in infile:
        lines += 1
        wordList = line.split()
        # loop words for total characters
        for word in wordList:
            words += 1
            characters += len(word)
        # calculate total characters / number of words
        averageChars = characters / words

    # print result
    print("The file contains", characters, "characters.")
    print("There are", words, "words in the file.")
    print("The average length of words is {0:0.1f} characters".format(averageChars)+".")
    print("The were", lines, "lines in the file.")

    # close files
    infile.close()


main()
