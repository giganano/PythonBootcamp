r""" 
The solution to problem 2. 
""" 

import numpy as np 


def part_a(): 
	r""" 
	Write the numbers 1 through 10000 to an output file along with their 
	squares, and the cube if the number is odd. 
	""" 
	with open("problem2.out", 'w') as f: 
		x = 1 
		while x <= int(1e4): 
			f.write("%d\t%d\t" % (x, x**2)) 
			if x % 2: # remember, numbers can be used in conditionals too 
				f.write("%d\t" % (x**3)) 
			f.write("\n") 
			x += 1 
		f.close() 


def part_b(): 
	r""" 
	Reads in the file generated from part a 
	""" 
	numbers = int(1e4) * [None] 
	with open("problem2.out", 'r') as f: 
		for i in range(len(numbers)): 
			# The split function turns a string into a list of strings, 'split' 
			# based on whitespace characters 
			numbers[i] = [int(i) for i in f.readline().split()] 
		f.close() 
	for i in range(20): print(numbers[i]) 


if __name__ == "__main__": 
	# this if condition shows up in code a lot - it ensures that you can import 
	# this file without actually running the functions 
	part_a() 
	part_b() 

