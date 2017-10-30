# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 5
# Programming Excercise 16

from graphics import *
from tkinter.filedialog import askopenfilename


def main():
    # get filenames
    infileName = askopenfilename()

    # open the files & create objects
    infile = open(infileName, "r")

    # create histogram count by line
    histogramData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in infile:
        histogramData[int(line)] += 1

    # Create a graphics window
    win = GraphWin("Student Quiz Score Histogram", 800, 700)
    win.setBackground("white")
    win.setCoords(-1, -1, 11, 11)

    # draw student names
    incrementX = 10 / len(histogramData)
    posX = 0
    for i in range(len(histogramData)):
        Text(Point(posX+0.5, -0.5), i).draw(win)
        count = Rectangle(Point(posX+0.1, 0), Point(posX+0.8, 0+histogramData[i]))
        count.draw(win)
        posX += incrementX

    # End Program
    endText = Text(Point(5, 5), "Click again to quit.")
    endText.setTextColor("red")
    endText.draw(win)
    win.getMouse()
    win.close()

    # Close file
    infile.close()


main()
