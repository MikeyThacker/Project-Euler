def get_month_days():
    reg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return reg, leap


def main():
    reg, leap = get_month_days()

    day = 2  # Day count - Tue 1 Jan 1901 = day 2
    count = 0  # Number of Sundays on first of month
    year = 1901  # Current Year

    while year != 2001:
        # Not Leap Year
        if year % 4 != 0:  # Is current year a leap year?
            for month in reg:
                day += month
                day_of_week = day % 7
                if day_of_week == 0:
                    count += 1

        # Leap year
        else:
            for month in leap:
                day += month
                day_of_week = day % 7
                if day_of_week == 0:
                    count += 1

        year += 1
    return count


print(main())

'''
Tuesday 1st Jan 1901 = day 1
7 days a week - sundays fall on day 7
any day % 7 == 0: is a sunday

Years are 365 days, leap years, 366
1900 not a leap year, 1904 is

first few years:
1901 - Not
1902 - Not
1903 - Not
1904 - Leap

main:
start from Tue 1st Jan 1901
add months to day Number, if % 7: count += 1
'''
