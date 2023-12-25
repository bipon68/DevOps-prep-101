
# leap year
year = input("Year: ")
year = int(year)

"""
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is leap year")
else:
    print(year, "is not a lear year")
"""

"""
if year % 4:
    if year % 100 and year % 400:
        print(year, "is leap year")
    elif year % 100 !=0:
        print(year, "is leap year")
    else: 
        print(year, "is not a leap year")
    print(year, "is leap year")
else:
    print(year, "is not a leap year")
"""

if year % 4 !=0:
    print(year, "is not a leap year")
elif year % 100 !=0:
    print(year, "is leap year")
elif year % 400 !=0:
    print(year, "is not a leap year")
else: 
    print(year, "is leap year")