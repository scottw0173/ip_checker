import csv
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

def make_list_ips(path: str = "./test.csv") -> list[str]:
    ips: list[str] = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header row
        for row in reader:
            ips.append(row[1].strip().strip('"'))
    return ips

