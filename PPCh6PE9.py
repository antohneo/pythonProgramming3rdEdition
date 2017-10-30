# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 9


def grade(score):
    # convert // lookup letter
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    return grades[score // 10]

def main():
    # print scale
    print("This program converts a test score (0-100) to the corresponding "
           + "letter grade.")

    # ask for input
    score = int(input("Enter a test score 0 - 100: "))


    # print result
    print("The score {0:0.0f} equals the letter grade of {1}.".format(score,
        grade(score)))

main()
