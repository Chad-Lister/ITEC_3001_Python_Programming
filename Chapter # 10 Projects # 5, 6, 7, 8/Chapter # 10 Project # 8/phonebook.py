"""
Program:  phonebook.py
Author:  Chad Lister
Date: 01/18/2021

This program defines the phonebook class and interface for the phonebook server program.

"""

import pickle

class PhoneNumber(object):

    def __init__(self, name, number):
        self._name = name
        self._number = number

    def getName(self):
        return self._name

    def getNumber(self):
        return self._number

    def __str__(self):
        result = "Name:  " + self._name + "\n"
        result += "Number:  " + self._number
        return result

class PhoneBook(object):

    def __init__(self, fileName = None):
        #self.data = []

        self._data = {}
        self._fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    phoneNumber = pickle.load(fileObj)
                    self._add(phoneNumber)
                except(EOFError):
                    fileObj.close()
                    break

    def add(self, phoneNumber):
        self._data[phoneNumber.getNumber()] = phoneNumber

    def remove(self, number):
        return self._data.pop(number)

    def get(self, number):
        return self._data.get(number)

    def __str__(self):
        return '\n'.join(map(str, self._data.values()))
   
    def save(self, fileName = None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName != None:
            self._fileName = fileName
        elif self._fileName == None:
            return
        fileObj = open(self._fileName, 'wb')
        for phoneNumber in self._data.values():
            pickle.dump(phoneNumber, fileObj)
        fileObj.close()
