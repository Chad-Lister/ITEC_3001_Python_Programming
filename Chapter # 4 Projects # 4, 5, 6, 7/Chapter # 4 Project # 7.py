"""
Program:  new_decryption.py
Author:  Chad Lister
Date: 12/18/2020

this program inverses the enryption from Chapter # 4 Project # 6

1.  Input is:
        encryptedString

2.  Computation is :
        if it's not blank
        split it into substrings
        shift substring 1 right
        convert shifted string from binary to decimal
        get character for decimal - 1
        add character to decrypted String
"""

# get user input
encryptedString = str(input("Please enter the encrypted string:  "))

# initialize variables
c = 0
count = 0
word = 0
stringLen = 0
digit = ""
index = 0
bit = ""
#ordNumber = 0
temp = ""
#char = ""
encChar = ""
tempString = ""
shiftedString = ""
convertedString = ""
decryptedString = ""
finalString = ""

# if  it's blank error
if len(encryptedString) == 0:
    print("Error.")

# else split
elif len(encryptedString) > 0:

    digitList = encryptedString.split()
    count = len(digitList)

    # for digits in list
    for digit in digitList:

        stringLen = len(digit)
        temp = digit[stringLen - 1]
        c += 1

        # shift right
        for index in range(len(digit) - 1):

            tempString += digit[index]
            index += 1
        shiftedString = temp + tempString
        temp = ""
        tempString = ""

        # convert shifted string
        decimal = 0
        exponent = len(shiftedString) - 1
        for bit in shiftedString:
            decimal = decimal + int(bit) * 2 ** exponent
            exponent -= 1

        # get character of number - 1
 
        ordNumber = decimal - 1
        encChar = chr(ordNumber)

        # add character to decrypted
        #decryptedString += encChar + " "
        decryptedString += encChar
        encChar = ""

        shiftedString = ""

    finalString += decryptedString
    decryptedString = ""
    #if c < count:
        #finalString = finalString + " " + decryptedString

    #decryptedString = decryptedString + " "
    #print(decryptedString)

    #elif c == count:
        
        #finalString += decryptedString

print(finalString)

