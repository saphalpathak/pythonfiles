def is_leap(year):
    if (year % 4 == 0 or year % 400 ==0):
        leap = True
    elif (year % 100 != 0 ):
        leap = False
    return leap

year = int(input())
print(is_leap(year))