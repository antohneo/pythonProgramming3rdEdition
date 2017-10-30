# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 4
# Programming Excercise 3


from graphics import *


def main():
    # Creates the window for the Face
    win = GraphWin("Space Face", 500, 500)
    center = Point(250, 250)

    # Draws face outline
    face = Oval(Point(100, 50), Point(400, 400))
    face.setFill(color_rgb(37, 31, 35))
    face.setOutline(color_rgb(37, 31, 35))
    face.draw(win)

    # Draws ovals for eyes
    lEye = Oval(Point(100, 200), Point(150, 250))
    lEye.setFill(color_rgb(223, 222, 222))
    lEye.setOutline(color_rgb(223, 222, 222))
    lEye.draw(win)

    rEye = lEye.clone()
    rEye.move(100, 0)
    rEye.draw(win)

    # Draw mouth
    mouth = Polygon(Point(150, 300), Point(300, 290),
                    Point(270, 330), Point(200, 350))
    mouth.setFill(color_rgb(252, 210, 2))
    mouth.draw(win)

    # End Program
    endText = Text(center, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()


main()
