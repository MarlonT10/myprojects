# -*- coding: utf-8 -*-
# Marlon Turcios
# Module 2 Assignment
"""
Created on 01/08/2022
Program to calcalate total wages for an employee for a week of work.
Marlon Turcios
Module 2 Assignment


"""
Employeename = ""
Hourlyrate = 0
Totalhours = 0

Totalwages = 0

Employeename = input("Please enter your name\n")
Hourlyrate = float(input(Employeename + ", what is your hourly rate?\n"))
Totalhours = int(input(Employeename + ", please enter the total hours worked this week.\n"))
Totalwages = float(Hourlyrate*Totalhours)

print(Employeename,", your check for this week should be $", Totalwages)



