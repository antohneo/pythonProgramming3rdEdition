# aaa
# python3 & zelle graphics.py module

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 16

from graphics import *
from math import sqrt

def calculateDistance(pointObj, center):
    # calculate slope
    slopeX = pointObj.getX() - center.getX()
    slopeY = pointObj.getY() - center.getY()
    if slopeX != 0:
        slope = slopeY / slopeX
        # calculate length
        length = sqrt(slopeX**2 + slopeY**2)
    else:
        length = pointObj.getY() - center.getY()
    return length


def main():
    # Creates the window for the Archery Target
    win = GraphWin("Archery Target", 500, 500)
    win.setCoords(-5, -5, 5, 5)
    center = Point(0, 0)

    # Draws 1st ring - white - maximum radius
    radius = 5
    first = Circle(center, radius)
    first.setFill("white")
    first.setOutline("black")
    first.draw(win)

    # Draws 2nd Ring - black - radius-1
    radius -= 1
    second = Circle(center, radius)
    second.setFill("black")
    second.setOutline("black")
    second.draw(win)

    # Draws 3nd Ring - blue - radius-1
    radius -= 1
    third = Circle(center, radius)
    third.setFill("blue")
    third.setOutline("black")
    third.draw(win)

    # Draws 4nd Ring - red - radius-1
    radius -= 1
    fourth = Circle(center, radius)
    fourth.setFill("red")
    fourth.setOutline("black")
    fourth.draw(win)

    # Draws 5nd Ring (center) - yellow - radius-1
    radius -= 1
    fifth = Circle(center, radius)
    fifth.setFill("yellow")
    fifth.setOutline("black")
    fifth.draw(win)

    # 5 rounds of clicks
    score = 0
    for i in range(1, 6):
        prompt = Text(Point(3, 4), "Click to take shot #{0}...".format(i))
        prompt.setFill("red")
        prompt.setSize(16)
        prompt.draw(win)
        scoreBox = Text(Point(-4, -4), "Score: {0}".format(score))
        scoreBox.setFill("black")
        scoreBox.setSize(16)
        scoreBox.draw(win)
        shot = win.getMouse()
        mark = Circle(shot, 0.1)
        mark.setFill("green")
        mark.draw(win)
        if calculateDistance(shot, center) < 1:
            score += 9
        elif calculateDistance(shot, center) < 2:
            score += 7
        elif calculateDistance(shot, center) < 3:
            score += 5
        elif calculateDistance(shot, center) < 4:
            score += 3
        elif calculateDistance(shot, center) < 5:
            score += 1
        else:
            score += 0
        prompt.undraw()
        scoreBox.undraw()


    # Get click to quit and close window
    scoreBox = Text(Point(-4, -4), "Score: {0}".format(score))
    scoreBox.setFill("black")
    scoreBox.setSize(16)
    scoreBox.draw(win)
    endText = Text(center, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()


main()
