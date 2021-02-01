"""
Program:  unique_words.py
Author:  Chad Lister
Date:  12/20/2020

This program get's input from a tex file, counts the word occurances, and lists the unique words
in alphabetical order.

1.  Input is:

        a text file

2.  Computation is:

        read file by line
        trim and split line
        remove punctuation
        put words into list
        sort the list
        for words in list put into dictionary with value 1.
        If already in dictionary, add 1 to value.
        If word is unique (value of 1) print it out

3.  Output is:

        the unique words in alphabetical order.
"""

# Get user input.
name = str(input("Please enter a text file's name:  "))
file = open(name, 'r')

# Read lines in file and put words into list.
# Remove new line and common punctuation.

punctuation = [",", ".", "?", "!", ";", ":", ")"]
wordList = []
words = ""

for line in file:
    
    line = line.strip()
    words = line.split()

    # For words in line.
    for word in words:

        # If last character is in punctuation list remove it.
        last = len(word) - 1
        character = word[last]
        if character in punctuation:
            word = word[0: last]
        else:
            word = word
            
        wordList.append(word)

# Sort list alphabetically.
wordList.sort()

# For words in list add to dictionary with value 1.
# If dictionary already contains word add 1 to count.
wordCount = {}

for word in wordList:

    count = wordCount.get(word, None)

    if count == None:

        wordCount[word] = 1
    else:
        wordCount[word] = count + 1

# Print the unique words.
print("The unique words in alphabetical order are:  ")
print("words only occuring once.")
print()

for (key, value) in wordCount.items():

    if value == 1:
        print("%-15s%8s" % (key, value))

# Print all words and counts.
print()
print("All words in alphabetical order and their total occurance's:  ")
print()
for (key, value) in wordCount.items():
    print("%-15s%8s" % (key, value))
