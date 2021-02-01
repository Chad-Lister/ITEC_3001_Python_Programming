"""
Program:  phoneserver.py
Author:  Chad Lister
Date: 01/20/2021

Server for a multi-client phone book.  

"""

from socket import *
from codecs import decode
from threading import Thread
from time import ctime
from phonebook import *

class ClientHandler(Thread):
    
    def __init__(self, client, phonebook):
        Thread.__init__(self)
        self._client = client
        self._phonebook = phonebook
        self._name = ""
        self._message = ""

    def run(self):
        self._client.send(bytes("Welcome to the phone book!", CODE))
        self._name = decode(self._client.recv(BUFSIZE), CODE)
        self._message = "Ready."
        self._client.send(bytes(str(self._message), CODE)) 
        
        while True:

            message = decode(self._client.recv(BUFSIZE), CODE)
            
            if len(message) > 1:
                
                for numbers in self._phonebook:
                    name = self._phonebook.getName()
                    if name == message:
                        num = self._phonebook.getNumber()
                        self._client.send(bytes(str(num), CODE))
                        
            else:
                obj = PhoneNumber(self._name)
                self._phonebook.add(PhoneNumber(obj))
                message = "number added!"
                self._client.send(bytes(str(message), CODE))
            elif not message:
                print("Client disconnected")
                self._client.close()
                break

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = "ascii"

phonebook = PhoneBook("phonebook.txt")
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("... connected from:", address)
    handler = ClientHandler(client, phonebook)
    handler.start()


