# -*- coding: utf-8 -*-
#Module 5 Assignment by Marlon Turcios
"""
Created on Wed Jan 19 09:11:44 2022
Program to show user a menu of options and verify their login credentials.
Marlon Turcios
Module 5 Assignment
Last Edit On January 20 2022
@author: Mvrlo
"""
CounterVar = 0

# This function checks user login information to verify that it is correct
def VerifyUser(IDVar, PassVar):
    if(IDVar == "admin" and PassVar == 2020):
        return True
    else:
        return False
    
# main() produces a user menu and calls the VerifyUser function depending on user input.
def main():
    global CounterVar
    Choice = 0
    UserID = ""
    Password = 0
    Result = 0
    
    print("Enter 1 to login.\n")
    print("Enter 2 to see About Page. \n")
    print("Enter 3 to end. \n")
    Choice = int(input("Enter your choice. \n"))
    
    if(Choice == 1):
        CounterVar+=1
        UserID = input("Please enter your user ID.\n")
        Password = int(input("Enter your password\n"))
        Result = VerifyUser(UserID, Password)
        if(Result == False and CounterVar == 3):
            print("The number of incorrect attempts is 3, goodbye. \n")
        elif(Result == True):
            print("Welcome.\n")
        else:
            print("\nThe number of incorrect attempts is ", CounterVar, ". \n")
            main()
    elif(Choice == 2):
        print("About: Our company is a large software startup founded in 2021.\n")
        main()
    elif(Choice == 3):
        print(" Goodbye.\n")
    else:
        print("That is not a valid option. PLease choose an option.\n")
        main()

main()
    
        
    
    
    
    
    