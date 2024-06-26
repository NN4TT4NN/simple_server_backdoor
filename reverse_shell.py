#!/usr/bin/python3
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 12345))
print("Connection stablished to server!")

while True:
    message = sock.recv(1024).decode()
    print(f"{message}")
    
    if message == "q":
        break
    else:
        message_back = input("Type Message To Send To Server: ")
        sock.send(message_back.encode())
sock.close()
