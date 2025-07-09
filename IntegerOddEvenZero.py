# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a file created by Rafael Molina
"""
 ##
 # A program that takes in an integer from the user and lets them know if the 
 #integer is a odd, even, or 0 as well as if its positive or negative
 #

#introduction to the program for the user
print("Hello! This program will let you know if your number is odd/even, positive/negative and if its a zero")

#variable created for the users input as a float number
varNum = float(input("Please enter your number: "))

#if conditions to determine if the number is 0, even or odd
if varNum == 0: 
    print("This number is 0! Which isn't odd, even, positive, or negative! Thank the Mayans")
elif varNum % 2 == 0:
    print("This number is even stevens and")
else:
    print("The number is odd and")
    
#if condition to determine if the number is positive or negative
if varNum > 0: 
    print("this number is positive! :)")
elif varNum < 0:
    print("this number is negative! :(")
    