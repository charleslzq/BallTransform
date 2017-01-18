import datetime
from os import path
from time import strptime, mktime

from xlrd import open_workbook

from SignRecord import SignRecord


def parse_xls_file(root, file):
    workbook = open_workbook(filename=path.join(root, file), encoding_override="GBK")
    person_record = parse_file_name(file)
    sheet = workbook.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        time_str = sheet.cell(i, 1).value
        time_tuple = strptime(time_str, '%Y/%m/%d %H:%M:%S')
        person_record.append(datetime.date.fromtimestamp(mktime(time_tuple)),
                             datetime.time(time_tuple.tm_hour, time_tuple.tm_min, time_tuple.tm_sec, 0))
    return person_record


def parse_file_name(file):
    filename = file[:-4]
    month = filename[-6:]
    name = filename[:-6]
    return SignRecord(name, month)
