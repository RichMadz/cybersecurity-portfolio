import socket

HOST = "127.0.0.1"
PORT = 9999

def attempt_login(username, password):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(3)

        client.connect((HOST, PORT))

        message = f"{username}:{password}"
        client.send(message.encode())

        response = client.recv(1024).decode()
    

        client.close()

        return response
    except socket.timeout:
        print("[!] Timeout - server not responding")
        return None
    
    except Exception as e:
        print(f"[!] Error: {e}")
        return None
    

def brute_force():
    passwords = ["1234", "password", "admin", "secret123"]
    attempts = 0

    for pwd in passwords:
        attempts += 1
        print(f"[Attempt {attempts} Trying: {pwd}")

        response = attempt_login("admin", pwd)

        if response is None:
            continue

        if response == "SUCCESS":
            print(f"[+] Password found: {pwd} after {attempts} attempts")
            break
        else:
            print("[-] Failed")

if __name__ == "__main__":
    brute_force()