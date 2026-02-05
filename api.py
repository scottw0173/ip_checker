import csv
import requests
import os
from ip_finder import make_list_ips

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
if not API_KEY:
    raise RuntimeError("ABUSEIPDB_API_KEY is not set in your environment")

def run_api(list):
    results = []

    for ip in list:
        params = {
            "ipAddress": ip,
            "maxAgeInDays": 90
        }

        response = requests.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers={
                "Accept": "application/json",
                "Key": "API_KEY"
            },
            params=params,
            timeout=10
        )

        response.raise_for_status()
        results.append(response.json())
    print(results)
