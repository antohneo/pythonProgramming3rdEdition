# aaa
# python3 & zelle graphics.py module

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 17

# Program uses move function to move circle when clicking

from graphics import *


def moveTo(shape, newCenter):
    # shape is a graphics object that supports the getCenter method
    # newCenter is a point
    # moves shape so that newCenter is its center
    shape.undraw()
    shape = Circle(newCenter, 20)
    shape.setOutline("red")
    shape.setFill("red")
    return shape


def main():
    win = GraphWin("Shape Space", 500, 500)
    center = Point(250, 250)
    shape = Circle(center, 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        prompt = Text(Point(200, 200), "Click new center point...")
        p = win.getMouse()
        shape = moveTo(shape, p)
        shape.draw(win)
    endText = Text(Point(0, 0), "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()


main()
