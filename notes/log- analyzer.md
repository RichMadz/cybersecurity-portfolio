# 🔍 Log Analyzer

## 🎯 Purpose
Analyze log files to detect suspicious activity, specifically repeated failed login attempts.

---

## 🧠 Core Concepts

### Data Cleaning
- `.strip()` → removes whitespace from start/end
- `.lower()` → normalizes text for consistent matching

### Pattern Matching
- `regex` → extracts IP addresses from logs
- Example: `\d+\.\d+\.\d+\.\d+`

### Counting
- Dictionary used to track number of attempts per IP
- Example:
  attempts[ip] = attempts.get(ip, 0) + 1

---

## ⚙️ Program Flow

1. Read log file line by line  
2. Clean each line (`strip`)  
3. Normalize (`lower`)  
4. Check for `"failed login"`  
5. Extract IP using regex  
6. Store and count attempts  
7. Print suspicious IPs  

---

## 🔑 Key Insights

- Normalize data before analysis  
- Separate cleaning → detection → counting  
- Don’t rely on exact string match (case issues)  
- Dictionaries are powerful for tracking patterns  

---

## 🧠 Mental Model

Logs → Clean → Normalize → Extract → Count → Report

---

## 🔥 Real-World Connection

Used in:
- intrusion detection systems  
- SIEM tools  
- security monitoring  

---

## 💡 What I Learned

- Regex basics  
- Data normalization  
- Counting patterns efficiently  
- Structuring analysis pipelines  