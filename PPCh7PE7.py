# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 7


def main():
    hrStart = int(input("Enter what hour the sitter started: "))
    minStart = int(input("Enter how many minutes past the hour the sitter started: "))
    hrEnd = int(input("Enter what hour the sitter ended: "))
    minEnd = int(input("Enter how many minutes past the hour the sitter ended: "))

    if hrEnd <= 9:
        timeSat = hrEnd - hrStart + ((minEnd - minStart)/60)
        charges = timeSat * 2.5
    if hrEnd > 9:
        if hrStart < 9:
            regularTimeSat = 9 - hrStart - (minStart / 60)
            lowerTimeSat = hrEnd - 9 + (minEnd / 60)
        if hrStart >= 9:
            regularTimeSat = 0
            lowerTimeSat = hrEnd - hrStart + ((minEnd - minStart)/60)
        timeSat = regularTimeSat + lowerTimeSat
        charges = regularTimeSat * 2.5 + lowerTimeSat * 1.75

    print("The sitter stayed from {0}:{1:0>2} until {2}:{3:0>2}, or {4:0.02f} hours.".format(hrStart, 
        minStart, hrEnd, minEnd, timeSat))
    print("The resulted in charges of ${0:0.02f}".format(charges))

main()
