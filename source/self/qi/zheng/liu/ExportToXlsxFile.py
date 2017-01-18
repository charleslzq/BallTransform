import openpyxl

col_names = ['A', 'B', 'C', 'D']


def cell_name(col, row):
    return ''.join([col_names[col+1], row])


def export(filename, table):
    workbook = openpyxl.Workbook()
    workbook.create_sheet('考勤记录', 0)
    worksheet = workbook.worksheets[0]
    for row in range(len(table)):
        worksheet.append(table[row])
    workbook.save(filename)