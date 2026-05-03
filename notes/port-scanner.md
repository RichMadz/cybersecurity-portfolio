# 🌐 Port Scanner

## 🎯 Purpose
Identify open ports on a target system and detect running services.

---

## 🧠 Core Concepts

### Networking
- `socket` → communication with other machines
- TCP connection used (`SOCK_STREAM`)

### Port Scanning
- `connect_ex()` → attempts connection
- Returns `0` if port is open

### Timeout
- `settimeout(1)` → prevents long waiting

### Concurrency
- `ThreadPoolExecutor` → multiple scans at once
- Speeds up scanning significantly

---

## ⚙️ Program Flow

1. Take target input  
2. Loop through ports  
3. Try connection  
4. If open → store result  
5. After scanning → sort results  
6. Display clean output  

---

## 🔥 Features Built

- Multi-threaded scanning  
- Custom port ranges (`--start`, `--end`)  
- Service mapping (port → service name)  
- Banner grabbing (extra info from services)  
- File output option  

---

## 🔑 Key Insights

- Separate scanning from output  
- Store results before printing  
- Threads improve speed but need control  
- Output should be clean and meaningful  

---

## 🧠 Mental Model

Target → Scan → Detect → Store → Sort → Display

---

## 🔥 Real-World Connection

Similar to:
- `nmap`
- reconnaissance phase in penetration testing  

---

## 💡 What I Learned

- Socket programming basics  
- Concurrency with threads  
- CLI tools using argparse  
- Data formatting and presentation  