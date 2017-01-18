from source.self.qi.zheng.liu.ChooseFiles import choose_excel_files
from source.self.qi.zheng.liu.DateUtil import generate_dates, filter_times, time_to_str, date_to_str
from source.self.qi.zheng.liu.ExportToXlsxFile import export
from source.self.qi.zheng.liu.ParseXlsFile import parse_xls_file
from source.self.qi.zheng.liu.SignResult import SignResult
from os import path

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
            for valid_sign_time in valid_sign_times:
                if len(valid_sign_time) > 0:
                    sign_result.append(date_to_str(date), raw_sign_record.name, time_to_str(valid_sign_time[0]), '')
                else:
                    sign_result.append(date_to_str(date), raw_sign_record.name, '', '')
        new_file_name = ''.join([raw_sign_record.name, raw_sign_record.month, '考勤记录.xlsx'])
        export(path.join(files_with_root[0], new_file_name), sign_result.rows)


