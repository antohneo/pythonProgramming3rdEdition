# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 4
# Programming Excercise 8


from graphics import *
import math


def main():
    # Open line window
    win = GraphWin("Line", 500, 500)
    win.setBackground("white")
    win.setCoords(-11, -11, 11, 11)
    center = Point(0, 0)

    # Draw x and y axis
    xAxis = Line(Point(0, -10), Point(0, 10))
    xAxis.setArrow("both")
    xAxis.setWidth(3)
    xAxis.draw(win)
    yAxis = Line(Point(-10, 0), Point(10, 0))
    yAxis.setArrow("both")
    yAxis.setWidth(3)
    yAxis.draw(win)

    # Draw x grid
    for i in range(-10, 10):
        xGrid = Line(Point(i, -10), Point(i, 10))
        xGrid.setFill(color_rgb(125, 140, 136))
        xGrid.draw(win)
    # Draw y grid
    for i in range(-10, 10):
        yGrid = Line(Point(-10, i), Point(10, i))
        yGrid.setFill(color_rgb(125, 140, 136))
        yGrid.draw(win)

    # Take input clicks
    l1 = Text(center, "Click anywhere in window.")
    l1.setFill(color_rgb(153, 92, 102))
    l1.setSize(32)
    l1.draw(win)
    pt1 = win.getMouse()
    l1.undraw()

    l2 = Text(pt1, "Click anywhere in window.")
    l2.setFill(color_rgb(153, 92, 102))
    l2.setSize(32)
    l2.draw(win)
    pt2 = win.getMouse()
    l2.undraw()

    # Draw midpoint and line through click points
    lineDraw = Line(pt1, pt2)
    midpt = Circle(lineDraw.getCenter(), .2)
    midpt.setFill("cyan")
    midpt.draw(win)
    lineDraw.draw(win)

    # calculate slope
    slopeX = pt2.getX() - pt1.getX()
    slopeY = pt2.getY() - pt1.getY()
    slope = slopeY / slopeX
    # calculate length
    length = math.sqrt(slopeX**2 + slopeY**2)
    # print slope and length
    Text(Point(8, 10), "Slope is: " + str(round(slope, 2))).draw(win)
    Text(Point(8, 9), "Length is: " + str(round(length, 2))).draw(win)

    # End Program
    endText = Text(center, "Click again to quit.")
    endText.setSize(32)
    endText.setFill(color_rgb(237, 215, 19))
    endText.draw(win)
    win.getMouse()
    win.close()


main()
