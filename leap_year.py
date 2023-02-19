# To check wheater the given year is leap year or not 
# check it with the two 
def isleapyear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

print(isleapyear(2100))


def leapyr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
print(leapyr(2000))