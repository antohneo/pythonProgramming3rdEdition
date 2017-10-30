# aaa
# python3

# Python Programming: An Introduction to Computer Science
# Chapter 7
# Programming Excercise 12


def yearValid(year):
            if year > 0:
                print("Date is valid.")
            else:
                print("Year must be greater than 0.")


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
                yearValid(yearValid)
            else:
                return False
        
        elif month in thirtyOne:
            if 1 <= day <= 31:
                yearValid(year)
            else:
                return False
        elif month == 2:
            if leapYear(year) == True:
                if 1 <= day <= 29:
                    yearValid(year)
                else:
                    return False
            else:
                if 1 <= day <= 28:
                    yearValid(year)
                else:
                    return False
    else:
        return False


def main():
    date = str(input("Enter date (formatted mm/dd/yyyy): "))

    first = date.find("/")
    second = date.find("/", first+1)
    month = int(date[:first])
    day = int(date[first+1:second])
    year = int(date[second+1:])

    
    print(dateValid(month, day, year))


main()
