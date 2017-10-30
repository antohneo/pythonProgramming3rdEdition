# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 14


from tkinter.filedialog import askopenfilename, asksaveasfilename


def squareEach(nums):
    # nums is a list of numbers, function modifies the list by squaring each
    for i in range(len(nums)):
        nums[i] = float(nums[i]) ** 2


def sumList(nums):
    # nums is a list of numbers, function returns the sum of the list
    tot = 0
    for i in range(len(nums)):
        tot += float(nums[i])
    return tot


def main():
    # get filenames
    infileName = askopenfilename()

    # open the files & create objects
    infile = open(infileName, "r")

    # create list from text file
    dataList = []
    for line in infile:
        dataList.append(line[:-1])

    # square items
    squareEach(dataList)

    # print result
    print(sumList(dataList))


main()
