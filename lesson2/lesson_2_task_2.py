def is_year_leap(year_input):
    if year_input % 4 == 0:
        return True
    return False


year = int ( input ('Введите год: '))
result = is_year_leap (year)
print ( f"год {year}: {result}")