import datetime, time


valid_start_time = datetime.time(hour=8, minute=31, second=0,microsecond=0)
valid_end_time = datetime.time(hour=16, minute=30, second=0, microsecond=0)
moon_time = datetime.time(hour=12, minute=0, second=0, microsecond=0)

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
    sign_times.sort()
    morning_sign = []
    afternoon_sign = []
    for sign_time in sign_times:
        if sign_time < valid_start_time and len(morning_sign) == 0:
            morning_sign.append(sign_time)
    sign_times.sort(reverse=True)
    for sign_time in sign_times:
        if sign_time > valid_end_time and len(afternoon_sign) == 0:
            afternoon_sign.append(sign_time)
    return morning_sign, afternoon_sign


def date_to_str(date):
    return datetime.date.strftime(date, '%m/%d/%Y')


def time_to_str(sign_time):
    return datetime.time.strftime(sign_time, '%H:%M:%S %p')

