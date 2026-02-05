import os
import requests

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
if not API_KEY:
    raise RuntimeError("ABUSEIPDB_API_KEY is not set in your environment")

def run_api(ips):
    results = []

    for ip in ips:
        params = {"ipAddress": ip, "maxAgeInDays": 90}

        response = requests.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers={
                "Accept": "application/json",
                "Key": API_KEY
            },
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()
        results.append(data)

        # Compact, readable per-IP output
        d = data.get("data", {})
        print(f"{d.get('ipAddress')}: score={d.get('abuseConfidenceScore')}, reports={d.get('totalReports')}")

    return results
