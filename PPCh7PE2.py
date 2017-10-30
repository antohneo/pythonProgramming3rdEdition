# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 2


def main():
    print('This program gives letter grades for quiz scores 0-5.')
    quizScore = int(input('Enter a quiz score 0-5: '))
    if quizScore <= 1:
        letterGrade = 'F'
    elif quizScore == 2:
        letterGrade = 'D'
    elif quizScore == 3:
        letterGrade = 'C'
    elif quizScore == 4:
        letterGrade = 'B'
    else:
        letterGrade = 'A'
    print('The score of {0} is a letter grade of {1}.'.format(quizScore, 
        letterGrade)) 


main()
