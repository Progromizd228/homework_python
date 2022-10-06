from datetime import date
from datetime import timedelta
def captain_log(c_year, c_month, c_day, c_entries):
    d = 1
    log_date = date(c_year, c_month, c_day)
    log_entry = open('CaptainLog.txt', 'a')
    for note in c_entries:
        one_day = timedelta(days=d)
        log_entry.write("%s: %s\n" % (log_date, note))
        log_date = date(c_year, c_month, c_day)
        d += 1
        log_date += one_day
    log_entry.close()
captain_log(1912, 4, 15, ['LET\'S RAM THAT ICEBERG!!!', 'Lol just kiddin', 'Actually...',
'No, that\'s a stupid idea...'])