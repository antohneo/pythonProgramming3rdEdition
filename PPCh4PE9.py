# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 4
# Programming Excercise 9

from graphics import *
import math


def main():
    # Draw window
    win = GraphWin("Line", 800, 800)
    win.setBackground("white")
    win.setCoords(-11, -11, 11, 11)

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

    # Prompt with directions
    intro = Text(Point(-2.5, 8.5), "This draws a rectangle based on 2 clicks. Click to continue...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    intro = Text(Point(-6.5, 8.5), "Click first corner of rectangle")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)

    # Get top left corner
    top = win.getMouse()
    intro.undraw()

    # Get bottom right corner
    intro = Text(Point(-6.5, 8.5), "Click opposite corner of rectangle")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    bottom = win.getMouse()
    intro.undraw()
    # Draw rectangle
    rect = Rectangle(top, bottom)
    rect.setOutline(color_rgb(153, 92, 102))
    rect.setWidth(3)
    rect.draw(win)

    # Calculate length
    xRect = abs(top.getX() - bottom.getX())
    # Calculate width
    yRect = abs(top.getY() - bottom.getY())
    # perimeter = 2(length + width)
    perimeter = str(round(2 * (xRect + yRect), 2))
    # area = length * width
    area = str(round(xRect * yRect, 2))

    # Print perimeter
    perimeterWin = Text(Point(-6.5, 8.5), "The rectangle perimeter is:" + perimeter)
    perimeterWin.setFill(color_rgb(153, 92, 102))
    perimeterWin.setSize(15)
    perimeterWin.draw(win)
    # Print area
    areaWin = Text(Point(-6.5, 7.5), "The rectangle area is:" + area)
    areaWin.setFill(color_rgb(153, 92, 102))
    areaWin.setSize(15)
    areaWin.draw(win)

    # End Program
    endText = Text(Point(-4.5, 0.5), "Click again to quit.")
    endText.setSize(32)
    endText.setFill(color_rgb(237, 215, 19))
    endText.draw(win)
    win.getMouse()
    win.close()


main()
