"""
Program: doctorserver.py
Author:  Chad Lister
Date:  01/18/2021

Server for a therapy session. Handles multiple clients concurrently.  Modified by Chad Lister
Chapter # 10 Project # 7:
    Modify doctor to save to individual files by patient/client name.

"""

from socket import *
from codecs import decode
from threading import Thread
from office import *

class ClientHandler(Thread):
    """Handles a session between a doctor and a patient."""
    def __init__(self, client, dr):
        Thread.__init__(self)
        self._client = client
        self._dr = dr
        #office = Office("office.txt")

    def run(self):
        self._client.send(bytes(self._dr.greeting(), 'ascii'))
        while True:
            message = decode(self._client.recv(BUFSIZE), 'ascii')
            if not message:
                print('Client disconnected')
                self._client.close()
                break
            else:
                self._client.send(bytes(self._dr.reply(message), 'ascii'))

HOST = 'localhost'
PORT = 21567
ADDRESS = (HOST, PORT)
BUFSIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

office = Office("office.txt")

while True:
    print('Waiting for connection . . .')
    client, address = server.accept()
    print('... connected from:', address)
    dr = Doctor(address)
    office.add(dr)
    handler = ClientHandler(client, dr)
    handler.start()

office.save("office.txt")
