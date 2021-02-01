"""
Program:  chatrecord.py
Author:  Chad Lister
Date:  01/18/2021

Modify the chatrecord programs to save the record to a text file.  Load and save each message.

"""

import pickle

class Message(object):

    def __init__(self, message):
        self._message = ""
##
##    def getMessage(self):
##        return self._message
##
##    def setMessage(self, s):
##        self._message = s
##        return self._message

class ChatRecord:

    def __init__(self, fileName = None):
        self._data = []

        self._fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    message = pickle.load(fileObj)
                    self._add(message)
                except(EOFError):
                    fileObj.close()
                    break

    def add(self, s):
        self._data.append(s)

    def __str__(self):
        if len(self._data) == 0:
            return 'No messages yet!'
        else:
            return '\n'.join(self._data)

    def save(self, fileName = None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName != None:
            self._fileName = fileName
        elif self._fileName == None:
            return
        fileObj = open(self._fileName, 'wb')
        for message in self._data:
            pickle.dump(message, fileObj)
        fileObj.close()
   
