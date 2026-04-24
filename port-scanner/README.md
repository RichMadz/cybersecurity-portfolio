🔍 Python Port Scanner

A multi-threaded port scanner built in Python that identifies open ports, detects common services, and performs basic banner grabbing.

⸻

🚀 Features

* Scan target hosts for open TCP ports
* Multi-threaded scanning for faster performance
* Custom port range (--start, --end)
* Service detection (e.g., SSH, HTTP)
* Banner grabbing for additional information
* Optional file output

⸻

🧠 How It Works

The scanner follows a simple pipeline:

1. Takes user input (target + optional flags)
2. Scans ports using concurrent threads
3. Attempts TCP connections to each port
4. Collects results (open ports + service + banner)
5. Sorts and displays results cleanly

⸻

🛠️ Usage

Basic scan:
python3 port_scanner.py scanme.nmap.org

Custom port range:
python3 port_scanner.py scanme.nmap.org --start 20 --end 100

Save results to file:
python3 port_scanner.py scanme.nmap.org --output results.txt

📌 Example Output
=== Scan Results ===

[+] Port 22    | SSH        | SSH-2.0-OpenSSH_6.6.1p1 Ubuntu...
[+] Port 80    | HTTP       | HTTP/1.1 400 Bad Request...

🧩 Project Structure

* scan_port() → Handles individual port scanning
* main() → Handles input, threading, and output
* SERVICES → Maps ports to known services

⸻

⚠️ Disclaimer

This tool is intended for educational purposes only.
Only scan systems you own or have permission to test.

⸻

📚 What I Learned

* Socket programming basics
* Multi-threading with ThreadPoolExecutor
* Handling user input with argparse
* Structuring code into logical components
* Separating data collection from output