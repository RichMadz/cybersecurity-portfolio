import re
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")

    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument(
        "--threshold",
        type=int,
        default=3,
        help="Number of attempts before flagging as suspicious (default: 3)"
    )

    args = parser.parse_args()

    return args.logfile, args.threshold

def analyze_logs(log_file):
    attempts = {}

    try:
        with open(log_file) as file:
            for line in file:
                clean_line = line.strip()

                if "failed login" in clean_line.lower():
                    ip_match = re.findall(r"\d+\.\d+\.\d+\.\d+", clean_line)

                    if ip_match:
                        ip = ip_match[0]
                        attempts[ip] = attempts.get(ip, 0) + 1

    except FileNotFoundError:
        print(f"❌ Error: File '{log_file}' not found.")
        sys.exit()

    return attempts


def print_results(attempts, threshold):
    sorted_attempts = sorted(attempts.items(), key=lambda x: x[1], reverse=True)

    print("\n=== Log Analysis Results ===\n")
    for ip, count in sorted_attempts:
        print(f"{ip}: {count} failed attempts")

    print("\n=== Suspicious Activity ===\n")
    for ip, count in sorted_attempts:
        if count >= threshold:
            print(f"⚠️ ALERT: {ip} → {count} failed attempts")


def save_results(attempts, threshold):
    sorted_attempts = sorted(attempts.items(), key=lambda x: x[1], reverse=True)

    with open("results.txt", "w") as output:
        output.write("=== Log Analysis Results ===\n\n")

        for ip, count in sorted_attempts:
            output.write(f"{ip}: {count} failed attempts\n")

        output.write("\n=== Suspicious Activity ===\n\n")

        for ip, count in sorted_attempts:
            if count >= threshold:
                output.write(f"ALERT: {ip} → {count} failed attempts\n")


def main():
    print("=== Log Analyzer Started ===")

    log_file, threshold = parse_arguments()
    attempts = analyze_logs(log_file)

    print_results(attempts, threshold)
    save_results(attempts, threshold)

    print("\n=== Analysis Complete ===")


if __name__ == "__main__":
    main()
