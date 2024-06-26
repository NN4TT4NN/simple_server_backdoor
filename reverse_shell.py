#!/usr/bin/python3
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 12345))
print("Connection stablished to server!")

message = sock.recv(1024).decode()
print(f"{message}")
answer = "Hello Back!"
sock.send(answer.encode())
sock.close()

# sock.close()