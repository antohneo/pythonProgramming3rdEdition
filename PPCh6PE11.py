# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 6
# Programming Excercise 11


def squareEach(nums):
    # nums is a list of numbers, function modifies the list by squaring each
    for i in range(len(nums)):
        nums[i] = float(nums[i]) ** 2


def main():
    # Get list of numbers
    nums = str(input("Enter a list of numbers separated by commas:"))
    numList = nums.split(",")
    # square list
    squareEach(numList)
    # check transformation
    print(numList)


main()
