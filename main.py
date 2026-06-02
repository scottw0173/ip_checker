from file_management import ask_which_file
from open_file import file_to_file_type, open_file
from find_ip_column import isolate_column, validate_ips, identify_column
from api import run_api
from result_management import add_results, write_new_file

def main():
    filename = ask_which_file()
    filetype = file_to_file_type(filename)
    rows = open_file(filename)
    key_column = identify_column(rows)
    if key_column == -1:
        print(f"Could not identify an column for IP addresses in file: {filename}")
        return
    
    global_ips = validate_ips(isolate_column(rows))
    results = run_api(global_ips)
    write_new_file(add_results(rows, results, key_column), filename, filetype)
    print(f"Results written to ./results/results_{filename}")
    
if __name__ == "__main__":
    main()