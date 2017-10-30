# python3
# python programming: an introducton to computer science
# chapter 1 programming excercise 7


def main():
    print("This prigram illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    print ("Input 1: ", x, "| Input 2: ", y)
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * (y - y * y)
        print (x, "|", y)


main()