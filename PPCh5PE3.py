# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 3


def main():
    # print scale
    print("This program converts a test score (0-100) to the corresponding "
           + "letter grade.")

    # ask for input
    score = int(input("Enter a test score 0 - 100: "))

    # convert // lookup letter
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    # print result
    print("The score: ", score, " equals the letter grade of",
          grades[score // 10] + ".")

main()
