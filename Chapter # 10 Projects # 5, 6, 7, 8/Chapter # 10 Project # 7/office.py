"""
Program:  office.py
Author:  Chad Lister
Date: 01/18/2021

Chapter # 10 Project # 7:
    Modify doctor to save to individual files by patient/client name.
    
"""

import pickle
import random

class Doctor(object):

    QUALIFIERS = ['Why do you say that ', 'You seem to think that ',
                  'Did I just hear you say that ', 'Why do you believe that ' ]

    REPLACEMENTS = {'I': 'you', 'me': 'you', 'my': 'your',
                    'we': 'you', 'us': 'you', 'am': 'are',
                    'you': 'I', 'You': 'I'}

    HEDGES = ['Go on.', 'I would like to hear more about that.',
              'And what do you think about this?', 'Please continue.']

    def __init__(self, client):
        self._history = []
        self._client = client

    def getClient(self):    # need get history?
        return self._client

    def greeting(self):
        return 'Good morning, how can I help you today?'

    def farewell(self):
        return 'Have a nice day!'

    def reply(self, sentence):
        choice = random.randint (1, 10)
        if choice == 1:
            if len(self_.history) > 3:
                answer = 'Earlier you said that ' + \
                self._change_person(random.choice(history))
            else:
                answer = random.choice(Doctor.HEDGES)
        elif choice in (2,3,4,5):
            answer = random.choice(Doctor.QUALIFIERS) + \
            self._change_person(sentence)
        else:
            answer = random.choice(Doctor.HEDGES)
        self._history.append(sentence)
        return answer
        
    def change_person(self, sentence):
        oldlist = sentence.split()
        newlist = []
        for word in oldlist:
            if word in Doctor.REPLACEMENTS:
                newlist.append(Doctor.REPLACEMENTS[word])
            else:
                newlist.append(word)
        return " ".join(newlist)

class Office(object):
    """ Represents an office of doctor objects. """

    def __init__(self, fileName = None):

        self._doctors = {}
        self._fileName = fileName    # office.txt
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    doctor = pickle.load(fileObj)
                    self.add(doctor)
                except(EOFError):
                    fileObj.close()
                    break


    def add(self, doctor):
        """Inserts a doctor using client name as a key."""
        self._doctors[doctor.getClient()] = doctor

    def remove(self, client):
        return self._doctors.pop(client, None)

    def get(self, client):
        return self._doctors.get(client, None)

    def save(self, fileName = None):
      if fileName != None:
          self._fileName = fileName
      elif self._fileName == None:
          return
      fileObj = open(self._fileName, 'wb')
      for doctor in self._doctors.values():
          pickle.dump(doctor, fileObj)
      fileObj.close()
