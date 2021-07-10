#!/usr/bin/python
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",54321))

print("Connection Established to Server")
sock.close()
