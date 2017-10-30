# Tablespoons to Gram Conversion
# python3


def main():

    print("This program converts tablespoons to gram equivalent.")
    tablespoons = float(input("Enter the number of tablespoons: "))

    grams = 14.3 * tablespoons

    print(tablespoons, " tablespoon(s) are equal to ", grams, " grams.", sep="")
    input("[ Press the <Enter> key to quit. ]")

main()