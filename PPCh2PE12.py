# Calculator Program
# python3


def main():

# Explain the program
    print("------------------------------------------------")
    print("This program works as a mathematical calculator.")
# Explain how to enter expression
    print("It can add (+), subtract (-), multiply (*), divide (/),")
    print("use exponents (**), and modulus (//).")
    print("Enter a mathematical expression when prompted. E.g. 1000*10+5/22")
    print("The program will print out the answer then prompt for another expression.")
# Explain how to quit
    print("To quit, type 'quit()'.")

# Loop 100 times
    for j in range(100):
        # Prompt user for expression to calculate
        ans = eval(input("Type in a mathematical expression: "))
        # Print out answer
        print("The answer is", ans)

main()