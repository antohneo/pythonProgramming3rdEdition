# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 13


def yearValid(year):
            if year > 0:
                return True
            else:
                return False


def leapYear(year):
    century = year // 100
    if year % 4 == 0:
        if century % 4 == 0:
            return True
        else:
            return False
    else:
        return False


def dateValid(month, day, year):
    thirty = [4, 6, 9, 11]
    thirtyOne = [1, 3, 5, 7, 8, 10, 12]    
    if 1 <= month <= 12:
        if month in thirty:
            if 1 <= day <= 30:
                return yearValid(yearValid)
            else:
                return False
        
        elif month in thirtyOne:
            if 1 <= day <= 31:
                return yearValid(year)
            else:
                return False
        elif month == 2:
            if leapYear(year) == True:
                if 1 <= day <= 29:
                    return yearValid(year)
                else:
                    return False
            else:
                if 1 <= day <= 28:
                    return yearValid(year)
                else:
                    return False
    else:
        return False


def main():
    date = str(input("Enter date (formatted mm/dd/yyyy): "))

    first = date.find("/")
    second = date.find("/", first+1)
    m = int(date[:first])
    d = int(date[first+1:second])
    y = int(date[second+1:])

    if dateValid(m, d, y):
        daynum = 31*(m - 1) + d
        if m > 2:
            daynum - (4(m)+23)//10
        if leapYear(y):
            if m > 2:
                daynum += 1
        print(daynum)
    else:
        print("Not valid date.")


main()
