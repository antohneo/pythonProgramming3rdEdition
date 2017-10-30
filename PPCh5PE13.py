# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 13
# Calculates the average length of words in sentences

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print("This program creates a file of average word length in sentences.")

    # get filenames
    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    # open the files & create objects
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        wordList = line.split()
        # loop words for total characters
        totalChars = 0
        for word in wordList:
            totalChars += len(word)
        # calculate total characters / number of words
        averageChars = totalChars / len(wordList)
        # print result
        print("The average length of words in the sentence:", "'"+line+"'",
              "is {0:0.1f} characters".format(averageChars)+".", file=outfile)

    # close both files
    infile.close()
    outfile.close()


main()
