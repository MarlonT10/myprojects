# -*- coding: utf-8 -*-
# Module 4 Assignment by Marlon Turcios
"""
Created on Sat Jan 15 22:18:30 2022
Program to convert either Fahrenheit to Celsius or miles/hour to meters/second using functions.
Marlon Turcios
Module 4 Assignment
Last Edit on January 16 2022

@author: Mvrlo
"""

# This function converts a Fahrenheit value to a Celsius value.
def fahrenheit_to_celsius(UserValue):
    CelsiusTemp = 0.0
    CelsiusTemp = float(((5/9)*(UserValue - 32)))
    print("The temperature in Celsius is ", CelsiusTemp)

# This function converts a speed value from miles/hour to meters/second.
def speed_conversion(SpeedValue):
    MetersPerSecond = 0.0
    MetersPerSecond = float(((SpeedValue * 1600)/3600))
    print("Your speed in meters per second is", MetersPerSecond)

# main() calls a previous functioning depending on user input of 1 or 2.
def main():
    MainInput = 0
    FahrenheitTemp = 0.0
    Miles = 0.0
    
    
    print("Enter 1 to convert Fahrenheit temperature to Celsius. \n")
    print("Enter 2 to convert speed from miles per hour to meters per second. \n")
    MainInput = int(input("Enter 1 or 2.\n"))
    
    if(MainInput == 1):
        FahrenheitTemp = float(input("Enter a temperature in Fahrenheit . \n"))
        fahrenheit_to_celsius(FahrenheitTemp)
    elif(MainInput == 2):
        Miles = float(input("Enter your speed in miles per hour.\n"))
        speed_conversion(Miles)
    else:
        print("Error, that is not a valid input. Please enter 1 or 2.\n")
    
main()
    

        
        
        
    

    
   
    
    
    
    
    
    
    
    
    
