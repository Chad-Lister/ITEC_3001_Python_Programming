"""
Program:  new_encryption.py
Author:  Chad Lister
Date: 12/16/2020

This program takes a string character's ordinal number + 1 and encrypts it into binary and shifts it 1 left.  Spaces are padded for multi-word encryption.

1.  Input is:

        originalString

2.  Computation is:
        if string isn't a single character

            if it's not blank
                convert to binary and shift left
            else pad output with blank
            add to final String
        else if it is a single character
            convert to bianary and shift

3.  Output is:

        the encrypted final string

"""

# Get user input

originalString = str(input("Please enter a string to encrypt:  "))

# Initialize variables

index = 0
char = ""
encryptedString = ""
substring = ""
finalString = ""
ordNumber = 0

# If not a single character

if len(originalString) > 1:
    
    # For characters in string

    #for index in range(len(originalString) - 1):

    for index in range(len(originalString)):

        char = originalString[index]
        ordNumber = ord(char)

        # If not blank add 1 and reset substring
        if ordNumber != 32:
            ordNumber += 1
            substring = ""

            # convert to binary
            while ordNumber > 0:
                remainder = ordNumber % 2
                ordNumber = ordNumber // 2
                substring = str(remainder) + substring
                encryptedString = substring #+ encryptedString

                
            # Shift encrypted 1 left
            tempChar = encryptedString[0]
            character = 0
            newChar = ""
            shiftedString = ""

            for character in range(len(encryptedString) -1):
                newChar = encryptedString[character + 1]
                shiftedString += newChar
                character += 1
            encryptedString = shiftedString + tempChar

        # Add encryptedString to final with padding and increament index
        finalString = finalString + " " + encryptedString

        #index += 1

# If only one character
elif len(originalString) == 1:

    char = originalString[0]
    ordNumber = ord(char)

    # If blank
    if ordNumber ==  32:
        finalString = "BLANK SPACE"
    else:

        #add 1
        ordNumber += 1

        # convert to binary
        while ordNumber > 0:
            remainder = ordNumber % 2
            ordNumber = ordNumber // 2
            substring = str(remainder)
            encryptedString = substring + encryptedString
        
        # Shift encrypted 1 left
        tempChar = encryptedString[0]
        character = 0
        newChar = ""
        shiftedString = ""

        for character in range(len(encryptedString) -1):
            newChar = encryptedString[character + 1]
            shiftedString += newChar
            character += 1

        # Add to final string
        finalString = shiftedString + tempChar

# Display result
print("The encrypted string is:  ", finalString)

