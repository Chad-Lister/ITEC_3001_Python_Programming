"""
Program:  palindrome.py
Author:  Chad Lister
Date:  01/28/2021

DS Chapter # 7 Project # 2:

    Write a program that uses a stack to test input strings to determine
    if they are a palindrome or not.

"""

#from arrays import Array
from arraystack import ArrayStack

def main():
    """ The main function. """

    wordStack = ArrayStack()

    # get input and variable declaration.
    word = str(input("Please enter a word:  "))
    tempString = ""
    bol = False

    # check length.
    if len(word) > 0:

        word = word.strip()
        count = len(word)
        #word = word.split()
        #print(word)

        # for characters in string.
        # load into stack.
        for c in range(count):
            #t = Array.getitem(c)
            wordStack.push(c)
            print(c)

        # for items in stack.
        # load into tempString.
        for i in range(len(wordStack)):
            temp = wordStack.pop()
            #temp = wordStack.peek()
            #n = wordStack(ArrayStack(Array._getitem(i)))
            t = chr(temp)
            print(t)
            c = str(temp)
            print(temp, "   ", c, "   ", t)
            tempString += str(temp)
            #tempString += t
        print(wordStack, "   ", tempString)

        if tempString in word:
            bol = True

    elif len(word) == 0:
        print("Word cannot be blank.")

    print("\nFor the word", word, ".  Is", tempString, "a palindrome", bol,".")
    return

main()
