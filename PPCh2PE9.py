# FtoC.py
# python3
# converts Farenheit to Celsius


def main():

    print("This program converts the temperature from Farenheit to Celsius.")
    farenheit = float(input("Enter a temperature in Farenheit: "))
    celsius = (5 / 9) * (farenheit - 32)

    print("The temperature in Celsius is", celsius, "degrees.")
    input("[ Press the <Enter> key to quit. ]")

main()