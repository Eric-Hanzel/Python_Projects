def turn_y_d(y):
    td = 0#total days
    iy = 1900#initial year
    while iy != y:
        if leap(iy):
            td = td + 366
        else:
            td = td + 365
        iy = iy + 1
    return td
"""Convert total years to total days and return total days"""
def turn_m_d(m, y):
    td = 0#total days
    im = 1#initial month
    while im != m:
        td = td + maxday(im,y)
        im = im + 1
    return td
"""Convert total months to total days and return total days"""
def cal_week(d,m,y):
    totaldays = turn_y_d(y) + turn_m_d(m,y) + d
    #Calculated from a given date to January 1, 1900 the total number of days
    if totaldays % 7 == 0:
        return 7
    else:
        return totaldays % 7
"""Calculate the day of the week for the given date and return it"""
def maxday(m,y):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    if m == 2:
        if leap(y):
            return 29
        else:
            return 28
"""Give a month and a year, then return the maximum number of days in that month"""
def leap(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False
"""Determine whether a given year is a leap year and return bool"""
def check_print(d):
    if d < 10:
        print("", str(d), end=" ")
    if d >= 10:
        print(str(d), end=" ")
"""If it is a single digit, print a space plus a numbe;
If it is a two-digit number, print the number directly"""
def printdate(w,m,y):
    a = cal_week(1, m, y)#What day of the week is the first of this month
    b = 7 - a + 2#Calculate the date of the first row of the number in the second column of the calendar
    d = 1
    while d != maxday(m,y) + 1:
        if cal_week(d,m,y) == w:#If the week corresponding to the date matches the given number of week
            if d < b:#If the given date is less than the date of the first row of the number in the second column of the calendar
                check_print(d)
            else:
                if d <= b + cal_week(1,m,y) - 2:
                    """If the given date is bigger than the date of the first row of the number in the second column of the calendar
                    and less than the date in the second column of the row where the first of the month is located """
                    print("  ", end=" ")
                    check_print(d)
                else:
                    check_print(d)
            d = d + 1
        else:
            d = d + 1
    print()
"""w is week; d is day; y is year.
Print a line of dates that meet the week criteria
For example, if the line is Monday, then each day of the month will be judged by the loop.
If it is Monday, it will be printed, if it is not, it will not be printed."""
def calendar(m,y):
    print("M",end=" ")
    printdate(1,m,y)
    print("T",end=" ")
    printdate(2,m,y)
    print("W", end=" ")
    printdate(3,m,y)
    print("T",end=" ")
    printdate(4,m,y)
    print("F", end=" ")
    printdate(5,m,y)
    print("S", end=" ")
    printdate(6,m,y)
    print("S", end=" ")
    printdate(7,m,y)
"""Print the dates in seven lines, Monday through Sunday"""
m = int(input("Please enter the month: "))
y = int(input("Please enter the year: "))
calendar(m,y)
input("Press enter to exit...")