# !/usr/bin/python -tt
# this program will print a square on screen

# import system library
import sys

# select with what you want to print the square
brick = input('Please provide your selected brick:')
# check the brick for more then one character(brick can't be more then one character)
lengthOfBrick = len(brick)

# now select the length/width of the square
width = int(input('Please provide the width in numeric value - 6 to 20:'))

#now check for proper brick input
if lengthOfBrick > 1 or lengthOfBrick < 1:
	print('->> You have provided more then one character for brick')
	print('->> Your brick has be resized to single character')
	brick = brick[0]
else:
	print ('You have provided correct brick input')

#now check for proper width input
if width > 20 or width < 6:
	print ('->> You have provided an out of range width!')
	print ('->> Width is set to max. limit')
	width = 20
else:
	print('You have provided correct width input.')

# now build the square
print('Here is your output :- ')
for i in range(1,int(width+1)):
	if i == 1 or i == int(width):
		print ((brick + ' ' )* width)
	else:
		print(brick + (' ' * (width*2-3)) + brick )
