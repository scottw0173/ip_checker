# IP Checker
A command-line tool that scans a file for IP addresses, checks each public IP against the AbuseIPDB API, and appends the results as new columns to a copy of the original file.

## Requirements
Python 3.10+
- requests
- openpyxl
- xlrd
- python-dotenv

## Setup

1. Clone the repository

```
git clone https://github.com/scottw0173/ip_checker.git
cd ip_checker
```

2. Install dependencies

`pip install -r requirements.txt`

3. Copy .env.example to .env and add your AbuseIPDB API key

`cp .env.example .env`

A free API key can be obtained at abuseipdb.com

## Usage
1. Drop your file into the files/ directory

2. Run the program
`python main.py`

3. Select your file from the prompt

4. Results will be written to the results/ directory as results_<original_filename>

Supported file formats: .csv, .tsv, .xls, .xlsx

## Notes
- AbuseIPDB free tier is limited to 1,000 requests per day. The program will warn you if your file contains 500 or more unique public IPs, but it does not track your total remaining for the day
- The program uses rows 2-6 (or rows 2 to the end for smaller documents) as a test sample. If there are duplicate IPs in these rows, the program may fail to find the column with IP addresses
- Private, loopback, and link-local IP addresses are automatically filtered out before querying the API
- Duplicate IPs are deduplicated before querying — each unique IP is only checked once regardless of how many times it appears in the file
- The program automatically detects which column contains IP addresses — no configuration needed
- IPv6 addresses are not currently supported

## Future Improvements
- IPv6 support
- CLI argument support via argparse so files can be passed directly rather than through an interactive prompt
- A score threshold flag to filter results and only append rows where the abuse confidence score exceeds a specified value
