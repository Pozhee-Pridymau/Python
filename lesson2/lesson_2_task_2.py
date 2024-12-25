def is_leap_year(year):
    if year % 4 == 0:
            return True
    return False
year = 2028
if is_leap_year(year):
    print("True.")
else:
    print("False.")