"""
Program:  chatclient.py
Author: Ken Lambert modified by Chad Lister
Date:  01/20/2021

Client for a multi-client chat room.  Will not run as is.
"""

from socket import *
from codecs import decode

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = 'ascii'

# gives name, address and code string errors.
name = ""
message = ""

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print(decode(server.recv(BUFSIZE), CODE))

# gives name not defined error. Message not defined and address in use  errors.
#name = " CHAD"

name = input('Enter your name: ')
server.send(bytes(name, 'ascii'))

while True:
    record = decode(server.recv(BUFSIZE), CODE)
    if not record:
        print("Server disconnected")
        break
    print(record)
    message = input('> ')
    if not message:
        break
    server.send(bytes(message + '\n', CODE))
server.close()
