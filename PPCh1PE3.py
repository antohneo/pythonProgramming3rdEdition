# python3
# python programming: an introducton to computer science
# chapter 1 programming excercise 3


def main():
    print("This prigram illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = x
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print("x is now", x)
        y = 3.9 * y * (1 - y)
        print("y is now", y)


main()