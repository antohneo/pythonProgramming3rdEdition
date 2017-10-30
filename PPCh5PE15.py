# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 5
# Programming Excercise 15

from graphics import *
from tkinter.filedialog import askopenfilename


def main():
    # get filenames
    infileName = askopenfilename()

    # open the files & create objects
    infile = open(infileName, "r")

    # enter n to determine window size
    nStudents = int(infile.readline())

    # Create a graphics window
    win = GraphWin("Student Exam Scores", 800, 700)
    win.setBackground("white")
    maxY = 100*nStudents
    win.setCoords(-1, -1, 120, maxY)

    # draw student names
    posY = 0
    increment = maxY / nStudents
    for i in range(nStudents):
        line = infile.readline()
        content = line.split()
        name = content[0]
        score = int(content[1])
        Text(Point(10, posY+increment/2), name).draw(win)
        scoreGraph = Rectangle(Point(15, posY), Point(score+15, posY+increment))
        scoreGraph.draw(win)
        posY += increment

    # End Program
    endText = Text(Point(50, maxY/2), "Click again to quit.")
    endText.setTextColor("red")
    endText.draw(win)
    win.getMouse()
    win.close()

    # Close file
    infile.close()


main()
