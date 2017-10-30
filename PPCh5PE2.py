# aaa
# Python Programming: An Introduction to Computer Science
# python3
# Chapter 5
# Programming Excercise 2

def main():
    # print scale
    print("This program converts a quiz score (0-5) to the corresponding letter grade.")

    # ask for input
    score = int(input("Enter a quiz score 0 - 5: "))

    # convert // lookup letter
    grades = ["F", "F", "D", "C", "B", "A"]
    # print result
    print("The score: ", score, " equals the letter grade of",
          grades[score]+".")

main()

