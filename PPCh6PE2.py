# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 6
# Programming Excercise 2


def main():
    verse("one", "eat a plum")
    verse("two", "enquire who")
    verse("three", "climb a tree")
    verse("four", "hold the door")
    verse("five", "keep it live")
    verse("six", "get its fix")
    verse("seven", "throw his arms toward heaven")
    verse("eight", "jump the gate")
    verse("nine", "draw a line")
    verse("ten", "bite the hen")

def verse(n, action):
    print("The ants go marching", n+" by "+n+",", "hurrah! hurrah!")
    print("The ants go marching", n+" by "+n+",", "hurrah! hurrah!")
    print("The ants go marching", n+" by "+n+",")
    print("The little one stops to", action+",")
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! "*3)
    print()


main()
