import re, ipaddress
def identify_column(rows: list[list[str]]) -> int:
    count = min(5, len(rows)-1)
    test_sample = rows[1:count+1]
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    column_count = len(test_sample[0])
    for i in range(column_count):
        for j in range(count):
            if not re.fullmatch(ip_pattern, test_sample[j][i]):
                break
        else:
            check_set = set()
            for j in range(count):
                check_set.add(test_sample[j][i])
            if len(check_set) == count:
                return i
    return -1

def isolate_column(rows: list[list[str]]) -> list[str]:
    column = identify_column(rows)
    ip_values = set()
    for i in range(len(rows)):
        ip_values.add(rows[i][column])
    return list(ip_values)

def validate_ips(ip_addresses: list[str]) -> list[str]:
    global_ips = []
    for ip in ip_addresses:
        try:
            if ip.is_global:
                global_ips.append(ip)
        except ValueError:
            continue
    return global_ips