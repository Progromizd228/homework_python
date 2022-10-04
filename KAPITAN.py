from datetime import date
def captain_log(c_year, c_month, c_day, c_entry):
    log_date = date(c_year, c_month, c_day)
    log_entry = open('CaptainLog.txt', 'a')
    log_entry.write("%s: %s\n" % (log_date, c_entry))
    log_entry.close()
captain_log(1912, 4, 15, 'LET\'S RAM THAT ICEBERG!!!')