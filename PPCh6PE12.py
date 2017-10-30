# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 12


def sumList(nums):
    # nums is a list of numbers, function returns the sum of the list
    tot = 0
    for i in range(len(nums)):
        tot += float(nums[i])
    return tot


def main():
    # Get list of numbers
    nums = str(input("Enter a list of numbers separated by commas:"))
    numList = nums.split(",")
    # square list
    listTotal = sumList(numList)
    # check transformation
    print(listTotal)


main()