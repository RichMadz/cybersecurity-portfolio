# Log Analyzer (Python)

This project analyzes a log file to detect failed login attempts and identify suspicious IP addresses.

## Features

- Reads log files

- Detects failed login attempts

- Extracts IP addresses using regex

- Counts attempts per IP

- Flags suspicious IPs (3+ attempts)

## Example Output

192.168.1.10: 3 failed attempts  

⚠️ ALERT: 192.168.1.10 is suspicious with 3 attempts

```md
## How to Run

```bash

python3 log_analyzer.py

## Key Concepts
- File handling and log processing in Python
- Data normalization and filtering
- Regex-based pattern extraction
- Using dictionaries for tracking activity