import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
import argparse

# Port -> Service mapping
SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

# Shared results list
results = []

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        service = SERVICES.get(port, "Unknown")
    
        try:
            sock.send(b"Hello\r\n")
            banner = sock.recv(1024).decode().strip()
        except:
            banner = "No banner"

        results.append((port, service, banner))
        

    sock.close()


def main():
    parser = argparse.ArgumentParser(description="Port Scanner")

    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--output", help="Save results to file")

    args = parser.parse_args()

    target = args.target
    start_port = args.start
    end_port = args.end
    output_file = args.output
    

    print(f"\nScanning target: {target}")
    print(f"Ports: {start_port} - {end_port}\n")
    
    # Run threads
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port) 

    # Sort results after scanning
    sorted_results = sorted(results)

    
    print("\n=== Scan Results ===\n")

    lines = []

    for port, service, banner in sorted_results:
        line = f"[+] Port {port:<5} | {service:<10} | {banner}"
        print(line)
        lines.append(line)

    # Save to file if requested
    if output_file:
        with open(output_file, "w") as f:
            f.write("=== Scan Results ===\n\n")
            for line in lines:
                f.write(line + "\n")

        print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main() 