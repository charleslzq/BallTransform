import datetime, time


def generate_dates(month):
    start_date_str = ''.join([month, '01'])
    start_date_struct = time.strptime(start_date_str, '%Y%m%d')
    start_date = datetime.date(start_date_struct.tm_year, start_date_struct.tm_mon, start_date_struct.tm_mday)
    dates = []
    date_iterator = start_date
    while date_iterator.month == start_date.month:
        date_to_check = datetime.date(date_iterator.year, date_iterator.month, date_iterator.day)
        if date_to_check.isoweekday() <= 5:
            dates.append(date_to_check)
        date_iterator += datetime.timedelta(days=1)
    dates.sort()
    return dates


def filter_times(sign_times):
    valid_times = []
    valid_start_time = datetime.time(hour=8, minute=31, second=0,microsecond=0)
    valid_end_time = datetime.time(hour=16, minute=30, second=0, microsecond=0)
    for sign_time in sign_times:
        if sign_time < valid_start_time or sign_time > valid_end_time:
            valid_times.append(sign_time)
    valid_times.sort()
    return valid_times

