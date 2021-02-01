"""
Program:  chatserver.py
Author:  Chad Lister
Date:  01/18/2021

Server for a multi-client chat room.  Modified.
Chapter # 10 Project # 6:
    Suggest and implement a way for the client to receive a copy of
    the chat record even when nothing is said.

"""

from socket import *
from codecs import decode
from chatrecord import ChatRecord
from threading import Thread
from time import ctime

class ClientHandler(Thread):
    
    def __init__(self, client, record):
        Thread.__init__(self)
        self._client = client
        self._record = record
        self._name = ""
        self._message = ""

    def run(self):
        self._client.send(bytes('Welcome to the chat room!', CODE))
        self._name = decode(self._client.recv(BUFSIZE), CODE)
        self._client.send(bytes(str(self._record), CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            if not message:
                print('Client disconnected')
                
                # Added by Chad. send record to client at close.
                self._client.send(bytes(str(self._record), CODE))
                self._client.close()
                break
            else:
                message = self._name + ' ' + \
                          ctime() + '\n' + message
                self._record.add(message)
                self._client.send(bytes(str(self._record), CODE))


HOST = 'localhost'
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = 'ascii'

record = ChatRecord()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('Waiting for connection . . .')
    client, address = server.accept()
    print('... connected from:', address)
    handler = ClientHandler(client, record)
    handler.start()


