is_year_leap = input('Введите год!')
year = int(is_year_leap)
if(year % 4 == 0):
    print(True)
else:
    print(False)


def is_year_leap(year):
    if year % 4 == 0:
        return 'True'
    else:
        return 'False'
result = is_year_leap(year)

print('год', year, ":", result )