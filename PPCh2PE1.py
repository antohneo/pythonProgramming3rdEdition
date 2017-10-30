# python3
# python programming: an introducton to computer science
# chapter 2 programming excercise 1
# PPCh2PE1.py

# chaos program
# illustrates chaotic behavior


def main():
    print("This prigram illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)


main()