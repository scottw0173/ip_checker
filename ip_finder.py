import csv

def make_list_ips(path: str = "./test.csv") -> list[str]:
    ips: list[str] = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header row
        for row in reader:
            ips.append(row[1].strip().strip('"'))
    print(ips)
    return ips

