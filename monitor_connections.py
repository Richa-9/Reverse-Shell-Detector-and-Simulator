import psutil

def detect_reverse_shell(attacker_ip, attacker_port):
    print(f"Monitoring connections for potential reverse shell to {attacker_ip}:{attacker_port}...")
    while True:
        for conn in psutil.net_connections(kind='inet'):
            if conn.raddr and conn.raddr.ip == attacker_ip and conn.raddr.port == attacker_port:
                print(f"[!] Reverse shell detected: {conn}")
                return

if __name__ == "__main__":
    ATTACKER_IP = "172.19.19.167"
    ATTACKER_PORT = 4444
    detect_reverse_shell(ATTACKER_IP, ATTACKER_PORT)
