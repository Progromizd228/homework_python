def LeapChecker(c_day, c_month, c_year):

    if c_month < 1 or c_month > 12:
        raise Exception('Месяц, который вы ввели, не существует.')
    if c_month in (1, 3, 5, 7, 8, 10, 12):
        if c_day < 1 or c_day > 31:
            raise Exception('День, который вы ввели, не существует в данном месяце.')
    if c_month in (4, 6, 9, 11):
        if c_day < 1 or c_day > 30:
            raise Exception('День, который вы ввели, не существует в данном месяце.')
    if c_month == 2:
        if (c_year%100!=0 and c_year%4==0):
            if (c_day < 1 or c_day > 29):
                raise Exception('День, который вы ввели, не существует в данном месяце.')
        else:
            if (c_day < 1 or c_day > 28):
                raise Exception('День, который вы ввели, не существует в данном месяце.')
    if (c_year%100!=0 and c_year%4==0):
        print('Введенная вами дата соответствует високосному году.')
    else:
         print('Введенная вами дата не соответствует високосному году.')

i_day = input('Введите день: ')
i_month = input('Введите месяц: ')
i_year = input('Введите год: ')
print('Ваша дата: ' + i_day + '-' + i_month + '-' + i_year)
i_day = int(i_day)
i_month = int(i_month)
i_year = int(i_year)

LeapChecker(i_day,i_month,i_year)