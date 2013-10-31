# !/usr/bin/python -tt
# import system library
import sys

# simple numeric calculations
var1 = 45
var2 = 46
var3 = 47

# plus
var4 = var1 + var2 + var3
# print the sum of all three variables
print ("Add:",var4)

#user input
var5 = input("Please provide interger: ")
#view user input variable
print ("You typed:",var5)

# substraction
var6 = var3 - var1
print("Sub:",var6)

# multiply
var7 = var1 * var2
print("multiply:",var7)

# division
var8 = var2/var3
print ("division:",var8)

#critical calculations
var9 = pow(var1,2)
var10 = var9*(var2/var3)-var7+(var1*var6)
print ("complex:",var10)
