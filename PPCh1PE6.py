# python3
# python programming: an introducton to computer science
# chapter 1 programming excercise 6


def main():
    print("This prigram illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = x
    z = x
    for i in range(100):
        x = 3.9 * x * (1 - x)
        print("Original equation equals ", x)
        y = 3.9 * (y - y * y)
        print ("Version two equals ", y)
        z = 3.9 * z - 3.9 * z * z
        print ("Version three equals ", z)


main()