#Write a program in cube.py that takes the length of an edge (an integer) as input and prints the cube’s surface area
# as output. For this exercise, write a program that contains an introductory docstring. This documentation should
# describe what the program will do (analysis) and how it will do it (design the program in the form of a pseudocode
# algorithm). Include suitable prompts for all inputs, and label all outputs appropriately.
# After you have coded a program, be sure to test it with a reasonable set of legitimate inputs.
loop = True
while loop == True:
	unfilteredSideLength = input("Enter cube side length in any unit to find the surface area, or type 'end' to end "
	                             "the program:\n")
	if unfilteredSideLength == "end":
		break
	try:
		sideLength = float(unfilteredSideLength)
	except:
		Exception
		print('Invalid input')
		continue
	surfaceArea = (sideLength ** 2 * 6)
	surfaceArea = f"{surfaceArea:.0f}" if surfaceArea % 1 == 0 else surfaceArea
	print(f'\n({unfilteredSideLength}²)6 = {surfaceArea} units\n')
	