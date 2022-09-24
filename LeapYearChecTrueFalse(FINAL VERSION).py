def Leap_Checker(c_day, c_month, c_year):
    if c_year < 1:
        return False
    if c_month < 1 or c_month > 12:
        return False
    if c_month in (1, 3, 5, 7, 8, 10, 12):
        if c_day < 1 or c_day > 31:
            return False
    if c_month in (4, 6, 9, 11):
        if c_day < 1 or c_day > 30:
            return False
    if c_month == 2:
        if (c_year % 100 != 0 and c_year % 4 == 0) or c_year % 400 == 0:
            if (c_day < 1 or c_day > 29):
                return False
            else:
                return True
        elif (c_day < 1 or c_day > 28):
            return False
    else:
        return True

i_day = input('Введите день: ')
i_month = input('Введите месяц: ')
i_year = input('Введите год: ')
print('Ваша дата: ' + i_day + '-' + i_month + '-' + i_year)

if (Leap_Checker(int(i_day), int(i_month), int(i_year)) == True):
    print('Введенная вами дата существует')
else:
    print('Вы ввели некорректную дату.')