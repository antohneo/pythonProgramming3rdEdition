# avg2.py
#   A simple program to average three exam scores  
#   Illustrates use of multiple input


def main():
    print("This program computes the average of 3 exam scores.")

    score1, score2, score3 = eval(input("Enter 3 scores separated by commas: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

    input("Press the <Enter> ket to quit.")


main()
