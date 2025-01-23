"""
Program: cube.py
Author: Miles Butler
Creation Date: 1/22/14
Intended Interpreter: Python Version 3.13

OVERVIEW:
    This is a program that gets a cube sidelength as a user input,
  then outputs the total surface area of the theoretical cube.

ASSIGNMENT INSTRUCTIONS
  Write a program in cube.py that takes the length of an edge (an integer) as input and prints
  the cube’s surface area as output. For this exercise, write a program that contains an introductory docstring. This
  documentation should
  describe what the program will do (analysis) and how it will do it (design the program in the form of a pseudocode
  algorithm). Include suitable prompts for all inputs, and label all outputs appropriately.
  After you have coded a program, be sure to test it with a reasonable set of legitimate inputs.

PSEUDOCODE
  Loop program until a "break" occurs.
  Get cube side length as a string.
  Print an exit message and break if the user inputs "end".
  Try to convert user input to floating point number.
  Restart loop if a Value Error occurs after sending a short error message.
  Restart loop if the user input is less than zero after sending a short error message.
  Calculate the surface area of the cube using the formula "sideLength² * 6"
  Initialize new value as "surfaceArea".
  Exclude the remainder if it's equal to zero.
  Print the cube's calculated surface area, along with the formula used to get it.
  Loop
"""

while True:
	unfilteredSideLength = input("Enter cube side length in any unit to find the surface area, or type 'end' to end "
	                             "the program:\n")
	if unfilteredSideLength == "end":
		print('Have a good one!')
		break
	try:
		sideLength = float(unfilteredSideLength)
	except ValueError:
		print('Invalid input')
		continue
	if sideLength < 0:
		print('Side length must be a positive number')
		continue
	surfaceArea = (sideLength ** 2 * 6)
	surfaceArea = f"{surfaceArea:.0f}" if surfaceArea % 1 == 0 else surfaceArea
	print(f'\nTotal Surface Area = ({unfilteredSideLength}²)6 = {surfaceArea} units \n')
	