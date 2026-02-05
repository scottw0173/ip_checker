from ip_finder import make_list_ips
from api import run_api

def main():
    ips = make_list_ips()
    run_api(ips)

if __name__ == "__main__":
    main()
