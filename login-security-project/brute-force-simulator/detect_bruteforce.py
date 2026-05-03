import sys
from collections import defaultdict
from datetime import datetime, timedelta

THRESHOLD = 5
WINDOW_SECONDS = 10

def parse_log(file):
    attempts = defaultdict(list)

    with open(file, "r") as f:
        for line in f:
            if "FAILED" in line:
                parts = line.split()
                timestamp_str = parts[0] + " " + parts[1]
                ip = parts[-1]

                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                attempts[ip].append(timestamp)

    return attempts


def detect_bruteforce(attempts):
    for ip, times in attempts.items():
        times.sort()

        for i in range(len(times)):
            window = times[i:i + THRESHOLD]

            if len(window) < THRESHOLD:
                continue

            if (window[-1] - window[0]).total_seconds() <= WINDOW_SECONDS:
                print(f"[!] {ip} → {THRESHOLD} attempts in {WINDOW_SECONDS}s")
                break


if __name__ == "__main__":
    log_file = sys.argv[1]
    attempts = parse_log(log_file)
    detect_bruteforce(attempts)