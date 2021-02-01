"""
Program:  chatclient.py
Author:  Chad Lister
Date:  01/18/2021

Server for a multi-client chat room.  Modified.
Chapter # 10 Project # 6:
    Suggest and implement a way for the client to receive a copy of
    the chat record even when nothing is said.

"""

from socket import *
from codecs import decode

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = 'ascii'
name = ""
record = ""
message = ""

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print(decode(server.recv(BUFSIZE), CODE))
name = input('Enter your name: ')
server.send(bytes(name, 'ascii'))

while True:
    record = decode(server.recv(BUFSIZE), CODE)
    if not record:
        print("Server disconnected")

        # Added by Chad.  Print after close.
        print(record)
        break
    print(record)
    message = input('> ')
    if not message:
        break
    server.send(bytes(message + '\n', CODE))
server.close()
