# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 8


def senator(age, citizenshipYears):
    if age < 30 or citizenshipYears < 9:
        return "Not eligible for US Senate."
    else:
        return "Eligible for US Senate."


def representative(age, citizenshipYears):
    if age < 25 or citizenshipYears < 7:
        return "Not eligible for US House."
    else:
        return "Eligibile for US House."


def main():
    age = int(input("Enter age in years: "))
    citizenshipYears = int(input("Enter the number of years of citizenship: "))

    print(senator(age, citizenshipYears))
    print(representative(age, citizenshipYears))


main()
