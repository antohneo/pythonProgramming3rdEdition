# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell


def main():


    print("Celsius:|Farenheit: ")
    for i in range(0, 110, 10):
        celsius = round(i, 2)
        fahrenheit = round(9 / 5 * celsius + 32, 2)
        print("   ", celsius, "  |   ", fahrenheit)

    input("Press the <Enter> key to quit.")


main()
