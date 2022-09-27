from datetime import date

def captain_log(c_year,c_month,c_day,c_entry):
    log_date = date(c_year, c_month, c_day)
    log_entry = open('CaptainLog.txt', 'a')
    log_entry.write("%s: %s\n" % (log_date, c_entry))
    log_entry.close()

in_year = int(input('Введите год: '))
in_month = int(input('Введите месяц: '))
in_day = int(input('Введите день: '))
in_entry = input('Введите ваше: ')
captain_log(in_year,in_month,in_day,in_entry)