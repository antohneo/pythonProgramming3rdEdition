# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell


def main():


    print("This program calculates temperature in Fahrenheit", end=" ")
    print("when given celsius. It executes 5 loops.")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9 / 5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    input("Press the <Enter> key to quit.")


main()
