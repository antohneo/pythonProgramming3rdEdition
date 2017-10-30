# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 1


def main():
    # summary of program
    print("This program calculates weekly wages based on 40 hr work week plus",
        "1.5x for time in excess of 40 hours.")
    # input number of hours worked
    hrs = float(input("Enter the number of hours worked: "))
    # input hourly rate
    rate = float(input("Enter the hourly salary rate: "))

    # calculate total wages for the week
    if hrs <= 40:
        wages = hrs * rate
    else:
        wages = 40 * rate + (hrs - 40) * rate * 1.5
    # print result
    print("The total wages due are ${0:0.02f}".format(wages))


main()
