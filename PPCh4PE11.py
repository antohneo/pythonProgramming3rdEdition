# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 4
# Programming Excercise 11 5 click house

from graphics import *
import math


def main():
    # Draw window
    win = GraphWin("5 Click House", 800, 800)
    win.setBackground("white")
    win.setCoords(-11, -11, 11, 11)

    # Prompt with directions
    intro = Text(Point(-2.5, 8.5), "This draws a house based on 5 clicks. Click to continue...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    win.getMouse()
    intro.undraw()
    intro = Text(Point(-2.5, 8.5), "The first 2 clicks are opposite corners of a rectangular frame")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    intro.undraw()
    intro = Text(Point(-6.5, 8.5), "Click bottom left corner of rectangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)

    # Get bottom left corner of frame
    one = win.getMouse()
    intro.undraw()

    # Get top right corner
    intro = Text(Point(-6.5, 8.5), "Click top right corner of rectangle...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    two = win.getMouse()
    intro.undraw()
    # Draw rectangle
    frame = Rectangle(one, two)
    frame.setOutline(color_rgb(153, 92, 102))
    frame.setWidth(3)
    frame.draw(win)

    # Get top center of door - 1/5 width of house frame
    intro = Text(Point(-6.5, 8.5), "Click top center of the doorway...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    three = win.getMouse()
    intro.undraw()
    # Calculate frame width
    doorWidth = abs( one.getX() - two.getX() ) / 5
    # Draw door
    door = Rectangle(Point(three.getX() + doorWidth / 2, three.getY()),
           Point(three.getX() - doorWidth / 2, one.getY()))
    door.setOutline(color_rgb(153, 92, 102))
    door.setWidth(3)
    door.draw(win)

    # Get center of window, 1/2 width of door
    intro = Text(Point(-6.5, 8.5), "Click center of the window...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    four = win.getMouse()
    intro.undraw()
    # Calculate frame width
    windowWidth = doorWidth / 2
    # Draw window
    window = Rectangle(Point(four.getX()- windowWidth/2, four.getY() - windowWidth/2),
             Point(four.getX()+ windowWidth/2, four.getY() + windowWidth/2))
    window.setOutline(color_rgb(153, 92, 102))
    window.setWidth(3)
    window.draw(win)

    # Get tip of roof
    intro = Text(Point(-6.5, 8.5), "Click tip of the triangular roof...")
    intro.setFill(color_rgb(153, 92, 102))
    intro.setSize(15)
    intro.draw(win)
    five = win.getMouse()
    intro.undraw()
    # Draw roof
    roof = Polygon(two, five, Point(one.getX(), two.getY()))    
    roof.setOutline(color_rgb(153, 92, 102))
    roof.setWidth(3)
    roof.draw(win)

    # End Program
    endText = Text(Point(-4.5, 0.5), "Click again to quit.")
    endText.setSize(32)
    endText.setFill(color_rgb(237, 215, 19))
    endText.draw(win)
    win.getMouse()
    win.close()


main()    