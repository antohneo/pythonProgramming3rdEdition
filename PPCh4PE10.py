# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 4
# Programming Excercise 10

from graphics import *
import math


def main():
    # Draw window
    win = GraphWin("Triangle", 800, 800)
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
    intro = Text(Point(-2.5, 8.5), "This draws a triangle based on 3 clicks. Click to continue...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    intro = Text(Point(-6.5, 8.5), "Click first corner of the triangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)

    # Get first corner
    a = win.getMouse()
    intro.undraw()

    # Get second corner
    intro = Text(Point(-6.5, 8.5), "Click second corner of the triangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    b = win.getMouse()
    intro.undraw()

    # Get third corner
    intro = Text(Point(-6.5, 8.5), "Click final corner of the triangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    c = win.getMouse()
    intro.undraw()

    # Draw rectangle
    tri = Polygon(a, b, c)
    tri.setOutline(color_rgb(153, 92, 102))
    tri.setWidth(3)
    tri.draw(win)

    # Calculate lengths
    ab = math.sqrt( (b.getX() - a.getX()) ** 2 + (b.getY()- a.getY()) ** 2)
    bc = math.sqrt( (c.getX() - b.getX()) ** 2 + (c.getY() - b.getY()) ** 2)
    ca = math.sqrt( (a.getX() - c.getX()) ** 2 + (a.getY() - c.getY()) ** 2)
    # Calculate s
    s = (ab + bc + ca) / 2
    # perimeter = 2(length + width)
    perimeter = str(round(ab + bc + ca, 2))
    # area = length * width
    area = str(round(math.sqrt(s * (s - ab) * (s - bc) * (s - ca)), 2))

    # Print perimeter
    perimeterWin = Text(Point(-6.5, 8.5), "The triangle perimeter is:" + perimeter)
    perimeterWin.setFill(color_rgb(153, 92, 102))
    perimeterWin.setSize(15)
    perimeterWin.draw(win)
    # Print area
    areaWin = Text(Point(-6.5, 7.5), "The triangle area is:" + area)
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
