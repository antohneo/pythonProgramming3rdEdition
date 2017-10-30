# aaa
# python3 

# Python Programming: An Introduction to Computer Science
# Chapter 8
# Programming Excercise 11


from tkinter.filedialog import askopenfilename 


def main():
    print("Program takes input of avg degrees on a given day in Farenheit.")
    print("If < 60, 60 - n = heating degrees. If > 80, n - 80 = cooling degrees.")
    print("Enter an average when prompted. To quit leave blank and hit <Enter>.")

    # open file
    infileName = askopenfilename()
    infile = open(infileName, "r")

    n = 0
    coolingN = 0 
    coolingTotal = 0
    heatingN = 0
    heatingTotal = 0

    for line in infile:
        dailyAvg = float(line)

        if dailyAvg < 60:
            heatingN += 1
            heatingTotal += 60 - dailyAvg
        elif dailyAvg > 80:
            coolingN += 1
            coolingTotal += dailyAvg - 80
        n += 1


    print("Out of {0} total days. {1} days were cooling days for a total of {2:0.2f} degrees.".format(
        n, coolingN, coolingTotal))
    print("{0} days were heating days for a total of {1:0.2f} degrees.".format(heatingN, heatingTotal))


main()
