# distanceToLightning
# program calculates the distance to a lightning strike
# based on the time elapsed between the flash and the sound of thunder
# python3


def main():
    print("This program calculates the distance to a lightning strike based")
    print("on the time elapsed between the flash and the sound of thunder.")
    timeElapsed = int(input("Number of seconds between flash and thunder: "))
    distanceToLightning = timeElapsed * 1100 / 5280
    print("The lightning is", round(distanceToLightning, 2), "miles away.")


main()
