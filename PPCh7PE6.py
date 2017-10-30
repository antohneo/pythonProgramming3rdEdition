# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 6


def main():
    speed = int(input("Enter the speed of the car in MPH: "))
    limit = 65
    if speed <= limit:
        fine = 0
        message = "You were under the speed limit."
        print(message)
    else:
        message = "You were over the limit by {0:0} MPH.".format(speed - limit)
        if speed <= 90:
            fine = 50.00 + 5 * (speed - limit)
        else:
            fine = 50.00 + 200 + 5 * (speed - limit)
        print(message, "Your fine is ${0:0.02f}".format(fine))


main()
