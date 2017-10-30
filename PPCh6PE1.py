# aaa
# Python Programming: An Introduction to Computer Science
# python3 & zelle graphics.py module
# Chapter 6
# Programming Excercise 1


def main():
    verse("cow", "moo")
    verse("hawk", "squawk")
    verse("chicken", "cluck")
    verse("dog", "bark")
    verse("tiger", "roar")


def verse(animal, sound):
    introOutro()
    print("And on that farm he had a", animal+",", "Ee-igh, Ee-igh, Oh!")
    print("With a", sound+", "+sound, "here and a", sound+", "+sound, "there.")
    print("Here a", sound, "there a", sound, "everwhere a", sound+", "+sound+".")
    introOutro()
    print()


def introOutro():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")


main()
