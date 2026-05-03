import time
import random
import socket

IPS = [
    "192.168.1.10",
    "192.168.1.15",
    "10.0.0.2",
    "172.16.0.5"
]

failed_attempts = {}
blocked_ips = {}
attempt_times = []
failed_user_attempts = {}

def load_users(file):
    users = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                username, password = line.split(":")
                users[username] = password
    return users


def log_attempt(username, success):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    ip = random.choice(IPS)

    if success:
        log_line = f"{timestamp} SUCCESS login from {ip}"
    else:
        log_line = f"{timestamp} FAILED login from {ip}"

    with open("login_attempts.log", "a") as log:
        log.write(log_line + "\n")


def authenticate(users, username, password):
    if username not in users:
        return None   # user doesn't exist

    if users[username] == password:
        return True

    return False


def main():
    users = load_users("users.txt")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9999))
    server.listen(1)

    print("Server listening on port 9999...\n")

    while True:
        # handshake
        client, addr = server.accept()
        ip = addr[0]
        current_time = time.time()

        # update and clean global timing
        attempt_times.append(time.time())

        # keeps only timestamps from the last 5 sec
        attempt_times[:] = [t for t in attempt_times if current_time - t < 5]
        if len(attempt_times) > 10:
            print("⚠️ Possible distributed attack detected")

        # 🔒 Block check
        if ip in blocked_ips and current_time < blocked_ips[ip]:
            print(f"Blocked IP attempted: {ip}")
            client.send("BLOCKED".encode())
            client.close()
            continue

        print(f"Connection from {addr}")

        # 📥 Receive data 
        data = client.recv(1024).decode().strip()
        print(f"DEBUG RECEIVED: {data}")

        if not data:
            client.close()
            continue

        # 🔍 Parse input
        try:
            username, password = data.split(":")
        except:
            client.send("Invalid format".encode())
            client.close()
            continue

        # 🔐 Authenticate
        success = authenticate(users, username, password)

        # 🧠 Adaptive delay
        attempts = failed_attempts.get(ip, 0)
        delay = min(attempts * 0.5, 5)
        time.sleep(delay)

        # 📊 Track attempts
        if not success:
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
            # incrememnt only on failure 
            failed_user_attempts[username] = failed_user_attempts.get(username, 0) + 1
        else:
            # reset penalty for success login for ip
            failed_attempts[ip] = 0
            # reset penalty for success login for username
            failed_user_attempts[username] = 0

        # 🚫 Block if needed
        if failed_attempts[ip] >= 5:
            blocked_ips[ip] = time.time() + 10
            print(f"IP {ip} blocked for 10 seconds")

        # 📝 Log
        log_attempt(username, success)

        # 📤 Respond
        response = "SUCCESS" if success else "FAILED"

        print(f"[{ip}] {username} → {response}")
        client.send(response.encode())

        client.close()


if __name__ == "__main__":
    main()
