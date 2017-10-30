# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 5


def main():
    print("This program calculates your BMI and checks if it falls in, below, or above the healthy range.")
    weight = float(input("Enter your weight in lbs: "))
    feet = float(input("Enter how many whole feet tall you are: "))
    inches = float(input("Enter how many inches (partial feet) tall you are: "))

    bmi = weight * 720 / ((feet * 12 + inches) ** 2)

    if bmi < 19:
        bmiRange = "below the healthy range."
    elif bmi <= 25:
        bmiRange = "in the healthy range."
    else:
        bmiRange = "above the healthy range."

    print("Your BMI is {0} and it falls {1}".format(bmi, bmiRange))


main()
