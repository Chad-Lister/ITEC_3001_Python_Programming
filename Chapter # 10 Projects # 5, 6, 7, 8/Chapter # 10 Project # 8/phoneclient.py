"""
Program:  phoneclient.py
Author:  Chad Lister
Date:  01/20/2021

Client for the online phone book assigment.  Gives the same errors as student files.

"""

from socket import *
from codecs import decode
from phonebook import PhoneNumber

HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"
name = ""
number = 0

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print(decode(server.recv(BUFSIZE), CODE))
nameIN = input("Enter a name to search for their number or 9 to add:  ")
if nameIN.isalpha() == True and len(nameIN) > 1:
    nameSearch = nameIN
elif int(nameIN) == 9:
    namePhone = str(input("Persons Name:  "))
    numberPhone = int(input("Phone Number (No spaces or dashes):  "))
    server.send(bytes(PhoneNumber(namePhone, numberPhone), "ascii"))
else:
    server.send(bytes(nameSearch, 'ascii'))

while True:
    number = decode(server.recv(BUFSIZE), CODE)
    if not number:
        print("Server disconnected")
        break
    print("Their number is:  ", number)
server.close()
