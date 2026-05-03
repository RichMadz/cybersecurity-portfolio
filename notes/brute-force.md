# 🔐 Brute Force Simulator

## 🎯 Purpose
Simulate password guessing attacks to understand brute force behavior.

---

## 🧠 Core Concepts

### Iteration
- Loop through password list

### File Handling
- Read passwords from file (`passwords.txt`)

### Logic
- Compare each password to correct one

### Delay Simulation
- `time.sleep(0.5)` → slows attempts

---

## ⚙️ Program Flow

1. Load password list  
2. Loop through passwords  
3. Attempt login  
4. If correct → stop  
5. If not → continue  
6. Print results  

---

## 🔥 Key Feature

```python
time.sleep(0.5)