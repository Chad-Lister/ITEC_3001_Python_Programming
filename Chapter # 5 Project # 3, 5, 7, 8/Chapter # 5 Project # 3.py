"""
Program:  modified_generator.py
Author:  Chad Lister
Date:  12/19/2020

This program modifies the generator.py program to use external files to build it's vocabulary
instead of tuples.  It includes the new function getWords that reads the file, generates a list,
converts the list to a tuple and returns the tuple for the 4 variables used in the program.

1. Input is:

        getWords("nouns.txt", r)
        getWords("verbs.txt", r)
        getWords("articles.txt", r)
        getWords("prepositions.txt", r)
    
2. Computation;

        randomly chosen:
        
        sentence = nounPhrase + verbPhrase
        nounPhrase = articles + nouns
        verbPhrase = verbs + nounPhrase + prepositionalPhrase
        prepositionalPhrase = preositions + nounPhrase
        
3. Output is:

        the randomly generated sentence
        
"""
import random
#import os

def getWords(fileName):
    """ Builds a list of tuples from a list inputed from an external file."""

    file = open(fileName, 'r')

    # Read from file and add to element list.
    elements = []
    for line in file:
        line = line.strip()
        words = line.split()

        for word in words:
            elements.append(str(word))

    # Change to tuple.
    tup = (elements)

    # Return tuple.
    return tup

articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

main()
