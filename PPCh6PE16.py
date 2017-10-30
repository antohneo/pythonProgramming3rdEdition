# aaa
# python3 & zelle graphics.py module

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 16

# Program draws faces over points clicked using function drawFace


from graphics import *
from math import sqrt


def drawFace(center, size, win):
    # center is a point - generated with a click
    # size is an int
    # win is a GraphWin

    # draw face outline
    face = Oval(Point(center.getX() - size, center.getY() - size), 
        Point(center.getX() + size, center.getY() + size))
    face.setFill(color_rgb(37, 31, 35))
    face.draw(win)

    # draw chest
    chest = Oval(Point(center.getX() - size * .50, center.getY() + size * .50), 
        Point(center.getX() + size * .45, center.getY() + size))
    chest.setFill(color_rgb(223, 222, 222))
    chest.draw(win)

    # draw eyes
    lEye = Oval(Point(center.getX() - size * .80, center.getY() - size * .20), 
        Point(center.getX() - size * .50, center.getY() + size * .20))
    lEye.setFill(color_rgb(223, 222, 222))
    lEye.draw(win)

    rEye = lEye.clone()
    rEye.move(size * .5, 0)
    rEye.draw(win)    
    # draw pupils
    lPupil = Oval(Point(center.getX() - size * .75, center.getY() - size * .10), 
        Point(center.getX() - size * .55, center.getY() + size * .20))
    lPupil.setFill(color_rgb(37, 31, 35))
    lPupil.draw(win)

    rPupil = lPupil.clone()
    rPupil.move(size * .5, 0)
    rPupil.draw(win)
    # draw beak
    topBeak = Polygon(Point(center.getX() - size * .80, center.getY() + size * .40), 
        Point(center.getX() - size * .40, center.getY() - size * .05), 
        Point(center.getX(), center.getY() + size * .40), 
        Point(center.getX() - size * .60, center.getY() + size * .50))
    topBeak.setFill(color_rgb(252, 210, 2))
    topBeak.draw(win)
    # draw nose
    lNostril = Oval(Point(center.getX() - size * .45, center.getY() + size * .10), 
        Point(center.getX() - size * .50, center.getY() + size * .18))
    lNostril.setFill(color_rgb(37, 31, 35))
    lNostril.draw(win)

    rNostril = lNostril.clone()
    rNostril.move(size * .12, 0)
    rNostril.draw(win)


def drawPointAtClick(center, win):
    centerPoint = Circle(center, 3)
    centerPoint.setFill("red")
    centerPoint.draw(win)
    return centerPoint


def textStyle(textObj, win):
    textObj.setTextColor(color_rgb(252, 85, 2))
    textObj.setStyle("bold")
    textObj.setSize(14)
    textObj.setFace("helvetica")
    textObj.draw(win)


def main():
    # open grapics win
    win = GraphWin("Faces", 666, 500)
    center = Point(333, 250)

    # load photo
    imageImported = Image(center, "faces.ppm")

    # display image in graphwin same width and height as image
    imageImported.draw(win)

    # how many faces are being blocked
    prompt = Text(Point(200, 200), "How many faces do you want to block?")
    textStyle(prompt, win)
    # create input box
    inputBox = Entry(Point(400, 200), 3)
    inputBox.setText("2")
    inputBox.draw(win)
    # create button & get click
    button = Text(Point(400, 250), "< Click to continue >")
    textStyle(button, win)
    win.getMouse()
    nFaces = int(inputBox.getText())

    # loop to create faces
    inputBox.undraw()
    button.undraw()
    for i in range(1, nFaces + 1):
        # click center
        prompt.setText("Click the center of face number {0}.".format(i))
        centerFace = win.getMouse()
        cfPoint = drawPointAtClick(centerFace, win)

        # click edge
        prompt.setText("Click the edge of face number {0}.".format(i))
        edgeFace = win.getMouse()
        efPoint = drawPointAtClick(edgeFace, win)

        # draw graphics in graphwin
        slopeX = edgeFace.getX() - centerFace.getX()
        slopeY = edgeFace.getY() - centerFace.getY()
        size = sqrt(slopeX**2 + slopeY**2)
        drawFace(centerFace, size, win)

        prompt.undraw()
        cfPoint.undraw()
        efPoint.undraw()

    # End Program
    endText = Text(center, "")
    textStyle(endText, win)
    win.getMouse()
    win.close()


main()
