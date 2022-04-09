# -*- coding: utf-8 -*-
# Module 8 Assignment by Marlon Turcios
"""
Created on Sun Jan 29 14:29:01 2022
Program to iterate over a string, cipher and decipher the string.
Marlon Turcios
Module 8 Assignment
Last Edit On January 30 2022
@author: Mvrlo
"""
#cipher receives a string and converts characters to their ASCI Code and concatenates them after adding the first character's ASCI code to them.
def cipher(StringInput):
    EachLetter = ""
    FirstLetter = ""
    FinalString = ""
    NewCharacter = ""
    Key = 0
    FirstLetter = StringInput[0]
    Key = ord(FirstLetter)
    
    for EachLetter in StringInput:
        NewCharacter = chr(ord(EachLetter) + Key)
        FinalString += NewCharacter
    return FinalString

#Decipher decodes the new string and rwverts it to the original string by means of a key.
def Decipher(StringValue):
    Letter = ""
    BeginningLetter = ""
    OriginalString = ""
    OriginalCharacter = ""
    DecipherKey = 0
    BeginningLetter = StringValue[0]
    DecipherKey = int((ord(BeginningLetter))/2)
    
    for Letter in StringValue:
        OriginalCharacter = chr(ord(Letter) - DecipherKey)
        OriginalString += OriginalCharacter
    return OriginalString

#main() calls the previous functions and receives string input and performs output.
def main():
    user_string = ""
    CipherResult = ""
    
    user_string = input("Enter a string.\n")
    CipherResult = cipher(user_string)
    print(CipherResult)
    DecipherResult = ""
    DecipherResult = Decipher(CipherResult)
    print(DecipherResult)
   
main()
        
        
    