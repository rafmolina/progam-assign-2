# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 22:04:55 2025

@author: rafae
"""

##
#This program takes in a roman numeral and outputs the product and sume of the 
# of the numbers in Arabic. This time the arabic will be ints instead of strings
#

# Code from program 2 is being reused, except the prints after each if comparison
# are not updating the variable that will hold the numbers in order to add and multiply

# the welcome to the user and letting them know what they're getting into
print("Hello, this program outputs the product and sum of two roman numerals!")
print("You will enter two roman numerals, they must be upper case, example: IV")
# this gets both inputs and places them into a variable
roman_numerals1 = input("Please enter your first roman numeral from 1-10:")
roman_numerals2 = input("Please enter your second roman numeral from 1-10:")

#the rules set for the first entery, turning the roman numerals into an int for arithmetic
num1 = 0
if roman_numerals1 == "I":
    num1 = 1
elif roman_numerals1 == "II":
    num1 = 2
elif roman_numerals1 == "III":
    num1 = 3
elif roman_numerals1 == "IV":
    num1 = 4
elif roman_numerals1 == "V":
    num1 = 5
elif roman_numerals1 == "VI":
    num1 = 6
elif roman_numerals1 == "VII":
    num1 = 7
elif roman_numerals1 == "VIII":
    num1 = 8
elif roman_numerals1 == "IX":
    num1 = 9
elif roman_numerals1 == "X":
    num1 = 10
else:
    print ("You did not enter a roman numeral")
#Same thing from the num1 except I named it num and not num2 cause i remembered num should have gone first
num = 0
if roman_numerals2 == "I":
    num = 1
elif roman_numerals2 == "II":
    num = 2
elif roman_numerals2 == "III":
    num = 3
elif roman_numerals2 == "IV":
    num = 4
elif roman_numerals2 == "V":
    num = 5
elif roman_numerals2 == "VI":
    num = 6
elif roman_numerals2 == "VII":
    num = 7
elif roman_numerals2 == "VIII":
    num = 8
elif roman_numerals2 == "IX":
    num = 9
elif roman_numerals2 == "X":
    num = 10
else:
    print ("You did not enter a roman numeral")
#The arithmetic for the outputs, the sum and product are placed in their own variable
sum_of_numerals = num1 + num
product_of_numerals = num1 * num
#this outputs what the program said it would, working good!
print("The sum of the numerals is: " , sum_of_numerals)
print("The product of the roman numerals entered are: " , product_of_numerals)


    
    