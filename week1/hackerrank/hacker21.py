#Write a function from hackerrank MEDIUM

def is_leap(year):
    leap = False
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    return True