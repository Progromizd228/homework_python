from datetime import date
from datetime import timedelta
def captain_log(c_year, c_month, c_day, c_entries):
    log_date = date(c_year, c_month, c_day)
    log_entry = open('CaptainLog.txt', 'a')
    one_day = timedelta(days=1)
    for note in c_entries:
        log_entry.write("%s: %s\n" % (log_date, note))
        log_date += one_day
    log_entry.close()
captain_log(1912, 4, 15, ['LET\'S RAM THAT ICEBERG!!!', 'Lol just kiddin', 'Actually...',
'No, that\'s a stupid idea...'])