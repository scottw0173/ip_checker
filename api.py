import os, requests, time
from dataclasses import dataclass

@dataclass
class IPResult:
    score: int
    reports: int
    country: str
    isp: str

API_KEY = os.getenv("ABUSEIPDB_API_KEY")
if not API_KEY:
    raise RuntimeError("ABUSEIPDB_API_KEY is not set in your environment")

def run_api(global_ips: list[str]) -> dict[str, IPResult]:
    results = {}
    if len(global_ips) >= 500:  #Check to make sure we don't overburden the API
        print(f"WARNING: this list is {round(len(global_ips) / 1000 * 100, 1)}% of free tier daily limit.")
        confirm = input("Continue? (y/n): ")
        if confirm.lower() != "y":
            return {}
    
    api_url = 'https://api.abuseipdb.com/api/v2/check'  #api url could need updating in the future
    api_headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    for ip in global_ips:
        api_params = {"ipAddress": ip, "maxAgeInDays": 90}
        response = requests.request(method='GET', url=api_url, headers=api_headers, params=api_params)

        response.raise_for_status()
        data = response.json()
        payload = data["data"]
        results[payload["ipAddress"]] = IPResult( #lots more data saved in 'payload' if you want to add it to the dictionary
            score=payload["abuseConfidenceScore"],
            reports=payload["totalReports"],
            country=payload["countryName"],
            isp=payload["isp"]
        )
        time.sleep(1)

    return results
