import socket
import os

def upload_file(ip, port, file_path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    with open(file_path, "rb") as file:
        data = file.read()
    sock.send(data)
    sock.close()

def download_file(ip, port, file_path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    with open(file_path, "wb") as file:
        data = sock.recv(1024)
        while data:
            file.write(data)
            data = sock.recv(1024)
    sock.close()

ip = "192.168.1.100"
port = 4444
file_path = "/path/to/file.txt"
upload_file(ip, port, file_path)
download_file(ip, port, file_path)