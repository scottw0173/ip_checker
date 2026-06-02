import csv, xlrd, openpyxl
from enum import Enum
from file_management import identify_extension

class FileType(Enum):
    CSV = "comma-separated-values"
    TSV = "tab-separated-values"
    XLS = "excel-classic"
    XLSX = "excel-modern"

def file_to_file_type(file: str) -> FileType:
    if identify_extension(file) == "csv":
        return FileType.CSV
    if identify_extension(file) == "tsv":
        return FileType.TSV
    if identify_extension(file) == "xls":
        return FileType.XLS
    if identify_extension(file) == "xlsx":
        return FileType.XLSX
    
def open_file(file: str) -> list[list[str]]:
    file_type = file_to_file_type(file)
    file_path = "./files/" + file
    rows: list[list[str]] = []
    if file_type == FileType.CSV:
        with open(file_path, mode='r',newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
    elif file_type == FileType.TSV:
        with open(file_path, mode='r',newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                rows.append(row)
    elif file_type == FileType.XLS:
        table = xlrd.open_workbook(file_path)
        reader = table.sheet_by_index(0)
        for row in range(reader.nrows):
            rows.append(reader.row_values(row))
    elif file_type == FileType.XLSX:
        table = openpyxl.load_workbook(file_path)
        reader = table.active
        for row in reader.iter_rows(values_only=True):
            rows.append(list(row))
    return rows