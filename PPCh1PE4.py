# python3
# python programming: an introducton to computer science
# chapter 1 programming excercise 4


def main():
    print("This prigram illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)


main()