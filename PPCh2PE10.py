# kilometersToMiles.py
# python3
# converts distance in kilometers to miles


def main():

    print("This program converts the distance in kilometers to miles.")
    kilometers = float(input("Enter a distance in kilometers: "))

    miles = round((0.62 * kilometers), 2)

    print(kilometers, " km is equal to ", miles, " miles.", sep="")
    input("[ Press the <Enter> key to quit. ]")

main()