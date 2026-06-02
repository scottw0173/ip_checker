import csv, openpyxl
from api import IPResult
from open_file import FileType

def add_results(rows : list[list[str]], results: dict[str, IPResult], key_column : int) -> list[list[str]]:
    rows[0].append("score")
    rows[0].append("reports")
    rows[0].append("country")
    rows[0].append("isp")
    for i in range(1, len(rows)):
        ip = rows[i][key_column]
        values = results.get(ip)
        if values:
            rows[i].append(values.score)
            rows[i].append(values.reports)
            rows[i].append(values.country)
            rows[i].append(values.isp)
        else:
            rows[i].append("N/A")
            rows[i].append("N/A")
            rows[i].append("N/A")
            rows[i].append("N/A")
    return rows

def write_new_file(rows: list[list[str]], filename:str, type: FileType):
    if type == FileType.CSV:
        new_filepath = "./results/results_" + filename 
        with open(new_filepath, 'w', newline='',encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    elif type == FileType.TSV:
        new_filepath = "./results/results_" + filename 
        with open(new_filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(rows)
    elif type == FileType.XLS or type == FileType.XLSX:
        new_filepath = "./results/results_" + filename
        wb = openpyxl.Workbook()
        ws = wb.active
        for row in rows:
            ws.append(row)
        wb.save(new_filepath)
