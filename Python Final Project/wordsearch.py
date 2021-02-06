"""
Program:  wordsearch.py
Author:  Chad Lister
Date:  02/05/2021

This program runs a word search GUI similar to the childrens puzzle game.


"""

from tkinter import *
from tkinter.font import *
import random

class WordSearch(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        
        Frame.__init__(self, bg = "#cccccc", highlightthickness = 1, highlightbackground = "black")
        self.master.title("Word Search")
        self.master.geometry("450x410")
        self.master.resizable(0, 0)
        self.grid()
        self._value1 = ""
        self._value2 = ""
        self._value3 = ""
        self._value4 = ""
        self._value5 = ""
        self._value6 = ""
        self._value7 = ""
        self._value8 = ""
        self._value9 = ""
        self._value10 = ""
        self._value11 = ""
        self._value12 = ""
        self._value13 = ""
        self._value14 = ""
        self._value15 = ""
        self._value16 = ""
        self._value17 = ""
        self._value18 = ""
        self._value19 = ""
        self._value20 = ""
        self._value21 = ""
        self._value22 = ""
        self._value23 = ""
        self._value24 = ""
        self._value25 = ""
        self._previous = 0
        self._next = 0
        self._boxCopy = []
        self._board1 =['GCOWS', 'RMORF', 'AJTUS', 'SNDAD', 'SNDCE'] 
        self._words1 = ['COWS', 'EAT', 'GRASS', 'DAD', 'AND', 'FROM']
        self._board2 = ['ESOOG', 'TRSOF', 'NNTNA', 'OXAOC', 'DSNCE']
        self._words2 = ['CAN', 'DONT', 'GOOSE', 'GOT', 'ANT', 'COAX']
        self._checkBox1 = StringVar()
        self._checkBox2 = StringVar()
        self._checkBox3 = StringVar()
        self._checkBox4 = StringVar()
        self._checkBox5 = StringVar()
        self._checkBox6 = StringVar()
        self._wordIndex = - 1
        self._playerInd = StringVar()
        self._message = ""
        self._score1 = IntVar()
        self._score2 = IntVar()
        self._wordCount = IntVar()
        self._rand = 0
        self._string = StringVar()
        self._playerOne = True
        self._playerTwo = False
        self._valid = False
        self._font = Font(family = "Verdana", size = 15)

        # Board frame.
        self._gamePane = Frame(self, highlightthickness = 5, highlightbackground = "black")
        self._gamePane.grid(row = 3, column = 0)

        # Word list frame.
        self._wordPane = Frame(self, bg = "white")
        self._wordPane.grid(row = 3, column = 10)

        # Checkbox frame.
        self._checkPane = Frame(self, bg = "white")
        self._checkPane.grid(row = 3, column = 12)

        # Command frame.
        self._commandPane = Frame(self, highlightthickness = 1, highlightbackground = "black")
        self._commandPane.grid(row = 10, column = 10)

        # Player frame.
        self._playerPane = Frame(self, bg = "#cccccc", highlightthickness = 1, highlightbackground = "black", padx = 10, pady = 10)
        self._playerPane.grid(row = 10, column = 0)
        self._player1 = Label(self._playerPane, font = self._font, text = "Player 1", bg = "#cccccc", fg = "red")
        self._player1.grid(row = 10, column = 0)
        self._scoreEntry1 = Entry(self._playerPane, textvariable = self._score1, width = 5, justify = "center", state = DISABLED)
        self._scoreEntry1.grid(row = 12, column = 0)
        self._player2 = Label(self._playerPane, font = self._font, text = "Player 2", bg = "#cccccc", fg = "red")
        self._player2.grid(row = 10, column = 8)
        self._scoreEntry2 = Entry(self._playerPane, textvariable = self._score2, width = 5, justify = "center", state = DISABLED)
        self._scoreEntry2.grid(row = 12, column = 8)

        # Word count frame.
        self._game = Frame(self, bg = "#cccccc", padx = 15, pady = 15, highlightthickness = 1, highlightbackground = "black")
        self._game.grid(row = 15, column = 0, rowspan = 4, columnspan = 10)
        self._wordCountText = Label(self._game, font = self._font, text = "Word Count", fg = "red", bg = "#cccccc")
        self._wordCountText.grid(row = 15, column = 1)
        self._wordCountLabel = Entry(self._game, font = self._font, width = 5, text = self._wordCount, fg = "red", bg = "#cccccc")
        self._wordCountLabel.grid(row = 15, column = 2)

        # Message frame.
        self._messagePane = Frame(self, bg = "#cccccc")
        self._messagePane.grid(row = 16, column = 10)

        self._loadList()
        self._loadBoard()
        
        return

    def _copy(self):
        """ Copies the list to box list. """

        if self._rand == 1:
            for i in range(len(self._words1)):
                self._boxCopy.append(self._words1[(i)])
        elif self._rand == 2:
            for i in range(len(self._words2)):
                self._boxCopy.append(self._words2[(i)])

        return
    
    def _clear(self):
        """ Clears the word and message. """

        self._string.set("")
        self._stringEntry = Entry(self._commandPane, textvariable = self._string, width = 8, state = DISABLED)
        self._stringEntry.grid(row = 13, column = 11)
        self._message = "                    "
        self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
        self._gameMSG.grid(row = 16, column = 10)
        self._previous = 0

        return

    def _do(self):
        """ Processes word, sets scores, display's messages and checks for the end of game. """

        self._message = "                    "
        self._gameMSG = Label(self._messagePane, font = self._font, text = self._message)
        self._gameMSG.grid(row = 16, column = 10)

        # Remove word from specific list.
        if self._rand == 1:
            self._valid = self._string.get() in self._words1
            if self._valid == True:
                word = self._string.get()
                self._wordIndex = self._boxCopy.index(word)
                self._words1.remove(word)
                self._wordCount.set(len(self._words1))
        elif self._rand == 2:
            self._valid = self._string.get() in self._words2
            if self._valid == True:
                word = self._string.get()
                self._wordIndex = self._boxCopy.index(word)
                self._words2.remove(word)
                self._wordCount.set(len(self._words2))

        # If player one and valid word and not blank.
        if self._playerOne == True and self._valid == True and self._string.get() != "":
            word = self._string.get()
            length = len(word)
            score = length + self._score1.get()
            self._score1.set(score)
            self._checkWin()
            self._string.set("")
            self._playerInd = "Player # 2"
            self._playerLabel = Label(self._commandPane, font = self._font, text = self._playerInd, fg = "blue")
            self._playerLabel.grid(row = 12, column = 10)
            self._playerOne = False
            self._playerTwo = True
            self._valid = False
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0
            self._buildBox()

        # If player two and valid word and not blank.
        elif self._playerTwo == True and self._valid == True and self._string.get() != "":
            word = self._string.get()
            length = len(word)
            score = length + self._score2.get()
            self._score2.set(score)
            self._checkWin()
            self._string.set("")
            self._playerInd = "Player # 1"
            self._playerLabel = Label(self._commandPane, font = self._font, text = self._playerInd, fg = "blue")
            self._playerLabel.grid(row = 12, column = 10)
            self._playerTwo = False
            self._playerOne = True
            self._valid = False
            self._message = "                     "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0
            self._buildBox()

        # Else theres an error.
        elif self._valid == False and self._string.get() != "":
            self._message = "Not in list!      "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:
            self._message = "Word is blank!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)

        return

    def _checkWin(self):
        """ Checks if the list is empty and game over. """

        lenList = self._wordCount.get()

        if lenList == 0:

            player1 = self._score1.get()
            player2 = self._score2.get()

            if player1 > player2:
                self._message = "Player # 1 Wins!"
                self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc", fg = "red")
                self._gameMSG.grid(row = 17, column = 10)
                
            elif player1 < player2:
                self._message = "Player # 2 Wins!"
                self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc", fg = "red")
                self._gameMSG.grid(row = 17, column = 10)
                
            elif player1 == player2:
                self._message = "Game Tied!"
                self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc", fg = "red")
                self._gameMSG.grid(row = 17, column = 10)
            
        return

    def _buildCommand(self):
        """ Builds the command box. """

        self._playerInd = "Player # 1"
        self._playerLabel = Label(self._commandPane, font = self._font, text = self._playerInd, fg = "blue")
        self._playerLabel.grid(row = 12, column = 10)
        self._wordLabel = Label(self._commandPane, font = self._font, text = "Word  :", fg = "red")
        self._wordLabel.grid(row = 13, column = 10)
        self._stringEntry = Entry(self._commandPane, textvariable = self._string, width = 8, state = DISABLED)
        self._stringEntry.grid(row = 13, column = 11)
        self._do = Button(self._commandPane, text = "DO", font = self._font, command = self._do)
        self._do.grid(row = 14, column = 10)
        self._clear = Button(self._commandPane, text = "Clear", font = self._font, command = self._clear)
        self._clear.grid(row = 14, column = 11)

        return

    def _buildBox(self):
        """ Builds the check box values. """

        # Change check box.
        if self._wordIndex == 0:
            self._checkBox1.set("*")
        elif self._wordIndex == 1:
            self._checkBox2.set("*")
        elif self._wordIndex == 2:
            self._checkBox3.set("*")
        elif self._wordIndex == 3:
            self._checkBox4.set("*")
        elif self._wordIndex == 4:
            self._checkBox5.set("*")
        elif self._wordIndex == 5:
            self._checkBox6.set("*")
            
        self._checkEntry = Entry(self._checkPane, font = self._font, textvariable = self._checkBox1, width = 2, justify = "right", state = DISABLED)
        self._checkEntry.grid(row = 4, column = 12)
        self._checkEntry2 = Entry(self._checkPane, font = self._font, textvariable = self._checkBox2, width = 2, justify = "right", state = DISABLED)
        self._checkEntry2.grid(row = 5, column = 12)
        self._checkEntry3 = Entry(self._checkPane, font = self._font, textvariable = self._checkBox3, width = 2, justify = "right", state = DISABLED)
        self._checkEntry3.grid(row = 6, column = 12)
        self._checkEntry4 = Entry(self._checkPane, font = self._font, textvariable = self._checkBox4, width = 2, justify = "right", state = DISABLED)
        self._checkEntry4.grid(row = 7, column = 12)
        self._checkEntry5 = Entry(self._checkPane, font = self._font, textvariable = self._checkBox5, width = 2, justify = "right", state = DISABLED)
        self._checkEntry5.grid(row = 8, column = 12)
        self._checkEntry6 = Entry(self._checkPane, font = self._font, textvariable = self._checkBox6, width = 2, justify = "right", state = DISABLED)
        self._checkEntry6.grid(row = 9, column = 12)

        return

    def _getPath(self):
        """ Marks the word path. """

        # Not yet implemented.

        return

    def _loadList(self):
        """ Loads the word list variables. """
        
        self._word = Label(self._wordPane, text = "Word List", font = self._font, bg = "white", fg = "red")
        self._word.grid(row = 3, column = 10)

        # Get random number for choice of board and word list.
        self._rand = random.randint(1, 2)
        if self._rand == 1:

            i = 1
            z = 4
            for i in range(len(self._words1)):
                self._word = self._words1[(i)]
                self._wordLabel = Label(self._wordPane, text = self._word, font = self._font, pady = 1)
                self._wordLabel.grid(row = z, column = 10)
                z += 1
                
            self._wordCount.set(len(self._words1))

        elif self._rand == 2:

            i = 1
            z = 4
            for i in range(len(self._words2)):
                self._word = self._words2[(i)]
                self._wordLabel = Label(self._wordPane, text = self._word, font = self._font, pady = 1)
                self._wordLabel.grid(row = z, column = 10)
                z += 1

            self._wordCount.set(len(self._words2))

        # Set initial values and build check boxes.
        self._checkBox1.set("")
        self._checkBox2.set("")
        self._checkBox3.set("")
        self._checkBox4.set("")
        self._checkBox5.set("")
        self._checkBox6.set("")
        self._copy()
        self._buildBox()

        # Build command box.
        self._buildCommand()

        return

    def _loadBoard(self):
        """ Loads the board variables. """

        board1 = []
        board2 = []
        board3 = []
        board4 = []
        board5 = []

        # Load board choice into lists.
        if self._rand == 1:
            board1 = self._board1[0]
            board2 = self._board1[1]
            board3 = self._board1[2]
            board4 = self._board1[3]
            board5 = self._board1[4]

        elif self._rand == 2:
            board1 = self._board2[0]
            board2 = self._board2[1]
            board3 = self._board2[2]
            board4 = self._board2[3]
            board5 = self._board2[4]

        self._gameBoard = Frame(self._gamePane, padx = 20, pady = 20, bg = "yellow")
        self._gameBoard.grid(row = 3, column = 0)

        i = 0

        # Load board values into containers.
        
        # First row (1 - 5).
        self._value1 = board1[(i)]
        self._value2 = board1[(i + 1)]
        self._value3 = board1[(i + 2)]
        self._value4 = board1[(i + 3)]
        self._value5 = board1[(i + 4)]

        # Second row (6 - 10).
        self._value6 = board2[(i)]
        self._value7 = board2[(i + 1)]
        self._value8 = board2[(i + 2)]
        self._value9 = board2[(i + 3)]
        self._value10 = board2[(i + 4)]

        # Third row (11 - 15).
        self._value11 = board3[(i)]
        self._value12 = board3[(i + 1)]
        self._value13 = board3[(i + 2)]
        self._value14 = board3[(i + 3)]
        self._value15 = board3[(i + 4)]

        # Fourth row (16 - 20).
        self._value16 = board4[(i)]
        self._value17 = board4[(i + 1)]
        self._value18 = board4[(i + 2)]
        self._value19 = board4[(i + 3)]
        self._value20 = board4[(i + 4)]

        # Fifth row (21 - 25).
        self._value21 = board5[(i)]
        self._value22 = board5[(i + 1)]
        self._value23 = board5[(i + 2)]
        self._value24 = board5[(i + 3)]
        self._value25 = board5[(i + 4)]

        # Put values into buttons and place on board.
        
        # First row (1 - 5).
        self._button1= Button(self._gameBoard, text = self._value1, padx = 10, pady = 10,
                              font = self._font, command = self._print1)
        self._button1.grid(row = 5, column = 2)
        self._button2 = Button(self._gameBoard, text = self._value2, padx = 10, pady = 10,
                               font = self._font, command = self._print2)
        self._button2.grid(row = 5, column = 3)
        self._button3 = Button(self._gameBoard, text = self._value3, padx = 10, pady = 10,
                               font = self._font, command = self._print3)
        self._button3.grid(row = 5, column = 4)
        self._button4 = Button(self._gameBoard, text = self._value4, padx = 10, pady = 10,
                               font = self._font, command = self._print4)
        self._button4.grid(row = 5, column = 5)
        self._button5 = Button(self._gameBoard, text = self._value5, padx = 10, pady = 10,
                               font = self._font, command = self._print5)
        self._button5.grid(row = 5, column = 6)

        # Second row (6 - 10).
        self._button6 = Button(self._gameBoard, text = self._value6, padx = 10, pady = 10,
                               font = self._font, command = self._print6)
        self._button6.grid(row = 7, column = 2)
        self._button7 = Button(self._gameBoard, text = self._value7, padx = 10, pady = 10,
                               font = self._font, command = self._print7)
        self._button7.grid(row = 7, column = 3)
        self._button8 = Button(self._gameBoard, text = self._value8, padx = 10, pady = 10,
                               font = self._font, command = self._print8)
        self._button8.grid(row = 7, column = 4)
        self._button9 = Button(self._gameBoard, text = self._value9, padx = 10, pady = 10,
                               font = self._font, command = self._print9)
        self._button9.grid(row = 7, column = 5)
        self._button10 = Button(self._gameBoard, text = self._value10, padx = 10, pady = 10,
                                font = self._font, command = self._print10)
        self._button10.grid(row = 7, column = 6)

        # Third row (11 - 15).
        self._button11= Button(self._gameBoard, text = self._value11, padx = 10, pady = 10,
                              font = self._font, command = self._print11)
        self._button11.grid(row = 9, column = 2)
            
        self._button12 = Button(self._gameBoard, text = self._value12, padx = 10, pady = 10,
                               font = self._font, command = self._print12)
        self._button12.grid(row = 9, column = 3)
        self._button13 = Button(self._gameBoard, text = self._value13, padx = 10, pady = 10,
                               font = self._font, command = self._print13)
        self._button13.grid(row = 9, column = 4)
        self._button14 = Button(self._gameBoard, text = self._value14, padx = 10, pady = 10,
                               font = self._font, command = self._print14)
        self._button14.grid(row = 9, column = 5)
        self._button15 = Button(self._gameBoard, text = self._value15, padx = 10, pady = 10,
                               font = self._font, command = self._print15)
        self._button15.grid(row = 9, column = 6)

        # Fourth row (16 - 20).
        self._button16 = Button(self._gameBoard, text = self._value16, padx = 10, pady = 10,
                               font = self._font, command = self._print16)
        self._button16.grid(row = 11, column = 2)
        self._button17 = Button(self._gameBoard, text = self._value17, padx = 10, pady = 10,
                               font = self._font, command = self._print17)
        self._button17.grid(row = 11, column = 3)
        self._button18 = Button(self._gameBoard, text = self._value18, padx = 10, pady = 10,
                               font = self._font, command = self._print18)
        self._button18.grid(row = 11, column = 4)
        self._button19 = Button(self._gameBoard, text = self._value19, padx = 10, pady = 10,
                               font = self._font, command = self._print19)
        self._button19.grid(row = 11, column = 5)
        self._button20 = Button(self._gameBoard, text = self._value20, padx = 10, pady = 10,
                                font = self._font, command = self._print20)
        self._button20.grid(row = 11, column = 6)

        # Fifth row (21 - 25).
        self._button21= Button(self._gameBoard, text = self._value21, padx = 10, pady = 10,
                              font = self._font, command = self._print21)
        self._button21.grid(row = 13, column = 2)
            
        self._button22 = Button(self._gameBoard, text = self._value22, padx = 10, pady = 10,
                               font = self._font, command = self._print22)
        self._button22.grid(row = 13, column = 3)
        self._button23 = Button(self._gameBoard, text = self._value23, padx = 10, pady = 10,
                               font = self._font, command = self._print23)
        self._button23.grid(row = 13, column = 4)
        self._button24 = Button(self._gameBoard, text = self._value24, padx = 10, pady = 10,
                               font = self._font, command = self._print24)
        self._button24.grid(row = 13, column = 5)
        self._button25 = Button(self._gameBoard, text = self._value25, padx = 10, pady = 10,
                               font = self._font, command = self._print25)
        self._button25.grid(row = 13, column = 6)

        return

    def _print1(self):
        """ Adds value1 to the string after checking if a valid move. """

        if self._previous == 2 or self._previous == 6 or self._previous == 7 or self._previous == 0:
            
            self._button1= Button(self._gameBoard, text = self._value1, padx = 10, pady = 10,
                                  font = self._font, command = self._print1, fg = "red")
            self._button1.grid(row = 5, column = 2)
            s = self._string.get()
            newString = s + self._value1
            self._string.set(newString)
            self._previous = 1
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:
            
            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print2(self):
        """ Adds value2 to the string after checking if valid move. """

        if self._previous == 1 or self._previous == 3 or self._previous == 6 \
           or self._previous == 7 or self._previous == 8 or self._previous == 0:

            self._button2 = Button(self._gameBoard, text = self._value2, padx = 10, pady = 10,
                                   font = self._font, command = self._print2, fg = "red")
            self._button2.grid(row = 5, column = 3)
            s = self._string.get()
            newString = s + self._value2
            self._string.set(newString)
            self._previous = 2
            self._message = "                 "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print3(self):
        """ Adds value3 to the string after checking if valid move. """

        if self._previous == 2 or self._previous == 4 or self._previous == 7 \
           or self._previous == 8 or self._previous == 9 or self._previous == 0:
            self._button3 = Button(self._gameBoard, text = self._value3, padx = 10, pady = 10,
                                   font = self._font, command = self._print3, fg = "red")
            self._button3.grid(row = 5, column = 4)
            s = self._string.get()
            newString = s + self._value3
            self._string.set(newString)
            self._previous = 3
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print4(self):
        """ Adds value4 to the string after checking if valid move. """

        if self._previous == 3 or self._previous == 5 or self._previous == 8 \
           or self._previous == 9 or self._previous == 10 or self._previous == 0:
            self._button4 = Button(self._gameBoard, text = self._value4, padx = 10, pady = 10,
                                   font = self._font, command = self._print4, fg = "red")
            self._button4.grid(row = 5, column = 5)
            s = self._string.get()
            newString = s + self._value4
            self._string.set(newString)
            self._previous = 4
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print5(self):
        """ Adds value5 to the string after checking if valid move. """

        if self._previous == 4 or self._previous == 9 or self._previous == 10 or self._previous == 0:
            self._button5 = Button(self._gameBoard, text = self._value5, padx = 10, pady = 10,
                                   font = self._font, command = self._print5, fg = "red")
            self._button5.grid(row = 5, column = 6)
            s = self._string.get()
            newString = s + self._value5
            self._string.set(newString)
            self._previous = 5
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return
    
    def _print6(self):
        """ Adds value6 to the string after checking if valid move. """

        if self._previous == 1 or self._previous == 2 or self._previous == 7 \
           or self._previous == 11 or self._previous == 12  or self._previous == 0:
            self._button6 = Button(self._gameBoard, text = self._value6, padx = 10, pady = 10,
                                   font = self._font, command = self._print6, fg = "red")
            self._button6.grid(row = 7, column = 2)
            s = self._string.get()
            newString = s + self._value6
            self._string.set(newString)
            self._previous = 6
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print7(self):
        """ Adds value7 to the string after checking if valid move. """

        if self._previous == 1 or self._previous == 2 or self._previous == 3 or self._previous == 6 \
           or self._previous == 8 or self._previous == 11 or self._previous == 12 or self._previous == 13 or self._previous == 0:
            self._button7 = Button(self._gameBoard, text = self._value7, padx = 10, pady = 10,
                                   font = self._font, command = self._print7, fg = "red")
            self._button7.grid(row = 7, column = 3)
            s = self._string.get()
            newString = s + self._value7
            self._string.set(newString)
            self._previous = 7
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print8(self):
        """ Adds value8 to the string after checking if valid move. """

        if self._previous == 2 or self._previous == 3 or self._previous == 4 or self._previous == 7 \
           or self._previous == 9 or self._previous == 12 or self._previous == 13 or self._previous == 14 or self._previous == 0:
            self._button8 = Button(self._gameBoard, text = self._value8, padx = 10, pady = 10,
                                   font = self._font, command = self._print8, fg = "red")
            self._button8.grid(row = 7, column = 4)
            s = self._string.get()
            newString = s + self._value8
            self._string.set(newString)
            self._previous = 8
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print9(self):
        """ Adds value9 to the string after checking if valid move. """

        if self._previous == 3 or self._previous == 4 or self._previous == 5 or self._previous == 8 \
           or self._previous == 10 or self._previous == 13 or self._previous == 14 or self._previous == 15 or self._previous == 0:
            self._button9 = Button(self._gameBoard, text = self._value9, padx = 10, pady = 10,
                                   font = self._font, command = self._print9, fg = "red")
            self._button9.grid(row = 7, column = 5)
            s = self._string.get()
            newString = s + self._value9
            self._string.set(newString)
            self._previous = 9
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0
            
        return

    def _print10(self):
        """ Adds value10 to the string after checking if valid move. """

        if self._previous == 4 or self._previous == 5 or self._previous == 9 or self._previous == 14 \
           or self._previous == 15  or self._previous == 0:
            self._button10 = Button(self._gameBoard, text = self._value10, padx = 10, pady = 10,
                                    font = self._font, command = self._print10, fg = "red")
            self._button10.grid(row = 7, column = 6)
            s = self._string.get()
            newString = s + self._value10
            self._string.set(newString)
            self._previous = 10
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print11(self):
        """ Adds value11 to the string after checking if valid move. """

        if self._previous == 6 or self._previous == 7 or self._previous == 12 \
           or self._previous == 16 or self._previous == 17  or self._previous == 0:
            self._button11= Button(self._gameBoard, text = self._value11, padx = 10, pady = 10,
                                  font = self._font, command = self._print11, fg = "red")
            self._button11.grid(row = 9, column = 2)
            s = self._string.get()
            newString = s + self._value11
            self._string.set(newString)
            self._previous = 11
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print12(self):
        """ Adds value12 to the string after checking if valid move. """

        if self._previous == 6 or self._previous == 7 or self._previous == 8 or self._previous == 11 \
           or self._previous == 13 or self._previous == 16 or self._previous == 17 or self._previous == 18 or self._previous == 0:
            self._button12 = Button(self._gameBoard, text = self._value12, padx = 10, pady = 10,
                                   font = self._font, command = self._print12, fg = "red")
            self._button12.grid(row = 9, column = 3)
            s = self._string.get()
            newString = s + self._value12
            self._string.set(newString)
            self._previous = 12
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print13(self):
        """ Adds value13 to the string after checking if valid move. """

        if self._previous == 7 or self._previous == 8 or self._previous == 9 or self._previous == 12 \
           or self._previous == 14 or self._previous == 17 or self._previous == 18 or self._previous == 19 or self._previous == 0:
            self._button13 = Button(self._gameBoard, text = self._value13, padx = 10, pady = 10,
                                   font = self._font, command = self._print13, fg = "red")
            self._button13.grid(row = 9, column = 4)
            s = self._string.get()
            newString = s + self._value13
            self._string.set(newString)
            self._previous = 13
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print14(self):
        """ Adds value14 to the string after checking if valid move. """

        if self._previous == 8 or self._previous == 9 or self._previous == 10 or self._previous == 13 \
           or self._previous == 15 or self._previous == 18 or self._previous == 19 or self._previous == 20 or self._previous == 0:
            self._button14 = Button(self._gameBoard, text = self._value14, padx = 10, pady = 10,
                                   font = self._font, command = self._print14, fg = "red")
            self._button14.grid(row = 9, column = 5)
            s = self._string.get()
            newString = s + self._value14
            self._string.set(newString)
            self._previous = 14
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print15(self):
        """ Adds value15 to the string after checking if valid move. """

        if self._previous == 9 or self._previous == 10 or self._previous == 14 \
           or self._previous == 19 or self._previous == 20 or self._previous == 0:
            self._button15 = Button(self._gameBoard, text = self._value15, padx = 10, pady = 10,
                                   font = self._font, command = self._print15, fg = "red")
            self._button15.grid(row = 9, column = 6)
            s = self._string.get()
            newString = s + self._value15
            self._string.set(newString)
            self._previous = 15
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0
        return
    
    def _print16(self):
        """ Adds value16 to the string after checking if valid move. """

        if self._previous == 11 or self._previous == 12 or self._previous == 17 \
           or self._previous == 21 or self._previous == 22  or self._previous == 0:
            self._button16 = Button(self._gameBoard, text = self._value16, padx = 10, pady = 10,
                                   font = self._font, command = self._print16, fg = "red")
            self._button16.grid(row = 11, column = 2)
            s = self._string.get()
            newString = s + self._value16
            self._string.set(newString)
            self._previous = 16
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print17(self):
        """ Adds value17 to the string after checking if valid move. """

        if self._previous == 11 or self._previous == 12 or self._previous == 13 or self._previous == 16 \
           or self._previous == 18 or self._previous == 21 or self._previous == 22 or self._previous == 23 or self._previous == 0:
            self._button17 = Button(self._gameBoard, text = self._value17, padx = 10, pady = 10,
                                   font = self._font, command = self._print17, fg = "red")
            self._button17.grid(row = 11, column = 3)
            s = self._string.get()
            newString = s + self._value17
            self._string.set(newString)
            self._previous = 17
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0
        
        return

    def _print18(self):
        """ Adds value18 to the string after checking if valid move. """

        if self._previous == 12 or self._previous == 13 or self._previous == 14 or self._previous == 17 \
           or self._previous == 19 or self._previous == 22 or self._previous == 23 or self._previous == 24 or self._previous == 0:
            self._button18 = Button(self._gameBoard, text = self._value18, padx = 10, pady = 10,
                                   font = self._font, command = self._print18, fg = "red")
            self._button18.grid(row = 11, column = 4)
            s = self._string.get()
            newString = s + self._value18
            self._string.set(newString)
            self._previous = 18
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0
            
        return

    def _print19(self):
        """ Adds value19 to the string after checking if valid move. """

        if self._previous == 13 or self._previous == 14 or self._previous == 15 or self._previous == 18 \
           or self._previous == 20 or self._previous == 23 or self._previous == 24 or self._previous == 25 or self._previous == 0:
            self._button19 = Button(self._gameBoard, text = self._value19, padx = 10, pady = 10,
                                   font = self._font, command = self._print19, fg = "red")
            self._button19.grid(row = 11, column = 5)
            s = self._string.get()
            newString = s + self._value19
            self._string.set(newString)
            self._previous = 19
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print20(self):
        """ Adds value20 to the string after checking if valid move. """

        if self._previous == 14 or self._previous == 15 or self._previous == 19 \
           or self._previous == 24 or self._previous == 25 or self._previous == 0:
            self._button20 = Button(self._gameBoard, text = self._value20, padx = 10, pady = 10,
                                    font = self._font, command = self._print20, fg = "red")
            self._button20.grid(row = 11, column = 6)
            s = self._string.get()
            newString = s + self._value20
            self._string.set(newString)
            self._previous = 20
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print21(self):
        """ Adds value21 to the string after checking if valid move. """

        if self._previous == 16 or self._previous == 17 or self._previous == 22 or self._previous == 0:
            self._button21= Button(self._gameBoard, text = self._value21, padx = 10, pady = 10,
                                  font = self._font, command = self._print21, fg = "red")
            self._button21.grid(row = 13, column = 2)
            s = self._string.get()
            newString = s + self._value21
            self._string.set(newString)
            self._previous = 21
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print22(self):
        """ Adds value22 to the string after checking if valid move. """

        if self._previous == 16 or self._previous == 17 or self._previous == 18 \
           or self._previous == 21 or self._previous == 23 or self._previous == 0:
            self._button22 = Button(self._gameBoard, text = self._value22, padx = 10, pady = 10,
                                   font = self._font, command = self._print22, fg = "red")
            self._button22.grid(row = 13, column = 3)
            s = self._string.get()
            newString = s + self._value22
            self._string.set(newString)
            self._previous = 22
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print23(self):
        """ Adds value23 to the string after checking if valid move. """

        if self._previous == 17 or self._previous == 18 or self._previous == 19 \
           or self._previous == 22 or self._previous == 24 or self._previous == 0:
            self._button23 = Button(self._gameBoard, text = self._value23, padx = 10, pady = 10,
                                   font = self._font, command = self._print23, fg = "red")
            self._button23.grid(row = 13, column = 4)
            s = self._string.get()
            newString = s + self._value23
            self._string.set(newString)
            self._previous = 23
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print24(self):
        """ Adds value24 to the string after checking if valid move. """

        if self._previous == 18 or self._previous == 19 or self._previous == 20 \
           or self._previous == 23 or self._previous == 25 or self._previous == 0:
            self._button24 = Button(self._gameBoard, text = self._value24, padx = 10, pady = 10,
                                   font = self._font, command = self._print24, fg = "red")
            self._button24.grid(row = 13, column = 5)
            s = self._string.get()
            newString = s + self._value24
            self._string.set(newString)
            self._previous = 24
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

    def _print25(self):
        """ Adds value24 to the string after checking if valid move. """

        if self._previous == 19 or self._previous == 20 or self._previous == 24 or self._previous == 0:
            self._button25 = Button(self._gameBoard, text = self._value25, padx = 10, pady = 10,
                                   font = self._font, command = self._print25, fg = "red")
            self._button25.grid(row = 13, column = 6)
            s = self._string.get()
            newString = s + self._value25
            self._string.set(newString)
            self._previous = 25
            self._message = "                    "
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
        else:

            self._message = "Illegal Move!"
            self._gameMSG = Label(self._messagePane, font = self._font, text = self._message, bg = "#cccccc")
            self._gameMSG.grid(row = 16, column = 10)
            self._previous = 0

        return

def main():
    """ The main function. """

    WordSearch().mainloop()

main()
