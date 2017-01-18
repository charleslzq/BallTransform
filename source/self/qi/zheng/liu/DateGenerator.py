import datetime, time


def generate_dates(month):
    start_date_str = ''.join([month, '01'])
    start_date_struct = time.strptime(start_date_str, '%Y%m%d')
    start_date = datetime.date(start_date_struct.tm_year, start_date_struct.tm_mon, start_date_struct.tm_mday)
    dates = []
    date_iterator = start_date
    while date_iterator.month == start_date.month:
        dates.append(datetime.date(date_iterator.year, date_iterator.month, date_iterator.day))
        date_iterator += datetime.timedelta(days=1)
    return dates

