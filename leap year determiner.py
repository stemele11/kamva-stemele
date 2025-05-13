from calendar import month

year = int(input('which year would you like to check if its a leap year  '))
month=int(input('enter the month    '))-1

def is_leap_year(year):
    """determine if a given year is a leap year."""
    if year % 4 ==0:
        if year % 100 ==0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False

def days_in_a_month(month):
    """Return days in a given month
    of particular year."""
    month_days=[31,28,31,30,31,30,31,30,31,31,30,31]

    if is_leap_year(year):
        if month==1 :
            return 29
    else:
        return month_days[month]


is_leap_year(year=year)
days=f'days in the {month+1} month of {year} are {days_in_a_month(month=month)}'
print(days)













