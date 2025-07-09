# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 21:45:55 2025

@author: rafae
"""
##
# This program turns roman numerals into arabic numerals 1-10. for example a 
# III should convert to a 3. 
# 

#The welcome to the user from the program
print("Hey there, welcome to the program that turns Roman Numerals in Arabic Numerals")
print("Note: Roman numerals are entered in upper case, for example: III")

#Creating the variable for each input that will be compared with an if statement
#Using snake case this time after reading up that python variables are preffered in snake
roman_numerals = input("Please enter a roman numeral from 1-10:")
#if statements that compare strings and move from 1 - 10 
if roman_numerals == "I":
    print("1")
elif roman_numerals == "II":
    print("2")
elif roman_numerals == "III":
    print("3")
elif roman_numerals == "IV":
    print("4")
elif roman_numerals == "V":
    print("5")
elif roman_numerals == "VI":
    print("6")
elif roman_numerals == "VII":
    print("7")
elif roman_numerals == "VIII":
    print("8")
elif roman_numerals == "IX":
    print("9")
elif roman_numerals == "X":
    print("10")
else:
    print ("You did not enter a roman numeral")
#Else to let the user know they did not input a valid number 