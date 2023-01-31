def LeapYear(year):
    if ((year %400) or (year%100 != 0 ) and (year%4 == 0) ):
        print('Leapyear')
    else:
        print('not')
year = int(input)

LeapYear(year)