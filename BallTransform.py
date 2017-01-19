from os import path

from ChooseFiles import choose_excel_files
from DateUtil import generate_dates, filter_times, time_to_str, date_to_str
from ExportToXlsxFile import export
from SignResult import SignResult
import datetime
from ParseXlsFile import parse_xls_file

valid_start_time = datetime.time(hour=8, minute=31, second=0,microsecond=0)
valid_end_time = datetime.time(hour=16, minute=30, second=0, microsecond=0)
files_with_root = choose_excel_files()

for filename in files_with_root[1]:
    if filename.endswith(".xls"):
        raw_sign_record = parse_xls_file(files_with_root[0], filename)
        sign_result = SignResult()
        sign_result.append('日期', '姓名', '时间', '备注')
        dates = generate_dates(raw_sign_record.month)
        for date in dates:
            sign_times = raw_sign_record.find_times_by_date(date)
            valid_sign_times = filter_times(sign_times)
            morning_sign = valid_sign_times[0]
            afternoon_sign = valid_sign_times[1]
            if len(morning_sign) == 0:
                sign_result.append(date_to_str(date), raw_sign_record.name, '', '缺席')
            elif morning_sign[0] > valid_start_time:
                sign_result.append(date_to_str(date), raw_sign_record.name, time_to_str(morning_sign[0]), '迟到')
            else:
                sign_result.append(date_to_str(date), raw_sign_record.name, time_to_str(morning_sign[0]), '')
            if len(afternoon_sign) == 0:
                sign_result.append(date_to_str(date), raw_sign_record.name, '', '缺席')
            elif afternoon_sign[0] < valid_end_time:
                sign_result.append(date_to_str(date), raw_sign_record.name, time_to_str(afternoon_sign[0]), '早退')
            else:
                sign_result.append(date_to_str(date), raw_sign_record.name, time_to_str(afternoon_sign[0]), '')
        new_file_name = ''.join([raw_sign_record.name, raw_sign_record.month, '考勤记录.xlsx'])
        export(path.join(files_with_root[0], new_file_name), sign_result.rows)


