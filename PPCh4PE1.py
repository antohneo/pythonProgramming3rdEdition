# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 4
# Programming Excercise 1


from graphics import *


def main():
    win = GraphWin()
    win.setCoords(-5, -5, 5, 5)
    shape = Rectangle(Point(-1, 1), Point(1, -1))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        newRectangle = shape.clone()
        p = win.getMouse()
        c = newRectangle.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newRectangle.move(dx, dy)
        newRectangle.draw(win)
    endText = Text(Point(0, 0), "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()


main()
