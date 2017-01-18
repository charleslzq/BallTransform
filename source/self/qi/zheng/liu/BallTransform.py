from source.self.qi.zheng.liu.ChooseFiles import choose_excel_files
from source.self.qi.zheng.liu.DateGenerator import generate_dates
from source.self.qi.zheng.liu.ParseXlsFile import parse_xls_file

files_with_root = choose_excel_files()
for filename in files_with_root[1]:
    if filename.endswith(".xls"):
        raw_sign_record = parse_xls_file(files_with_root[0], filename)
        dates = generate_dates(raw_sign_record.month)
        for date in dates:
            sign_times = raw_sign_record.find_times_by_date(date)
            print(date)
            print(sign_times)

