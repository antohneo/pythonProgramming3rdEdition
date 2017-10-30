# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 3


def main():
    print('This program gives letter grades for quiz scores 0-5.')
    examScore = int(input('Enter a quiz score 0-100: '))
    if examScore < 60:
        letterGrade = 'F'
    elif examScore < 70:
        letterGrade = 'D'
    elif examScore < 80:
        letterGrade = 'C'
    elif examScore < 90:
        letterGrade = 'B'
    else:
        letterGrade = 'A'
    print('The score of {0} is a letter grade of {1}.'.format(examScore, 
        letterGrade)) 


main()
