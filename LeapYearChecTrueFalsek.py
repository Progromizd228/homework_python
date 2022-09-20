def Leap_Checker(c_day, c_month, c_year):

    if (c_year % 100 != 0 and c_year % 4 == 0) or c_year % 400 == 0:
        return True
    else:
        return False

i_day = input('Введите день: ')
i_month = input('Введите месяц: ')
i_year = input('Введите год: ')
print('Ваша дата: ' + i_day + '-' + i_month + '-' + i_year)
i_day = int(i_day)
i_month = int(i_month)
i_year = int(i_year)

if (Leap_Checker(i_day, i_month, i_year) == True):
    print('Введенная вами дата соответствует високосному году.')
else:
    print('Введенная вами дата не соответствует високосному году.')