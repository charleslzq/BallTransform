from tkinter import filedialog
from os import listdir, path


def choose_excel_files():
    root_directory = filedialog.askdirectory()
    files = []
    for filename in listdir(root_directory):
        if filename.endswith(".xls") or filename.endswith(".xlsx"):
            files.append(filename)
    return root_directory, files








