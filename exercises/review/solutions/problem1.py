r""" 
The solution to problem 1. 
""" 

import numpy as np 


def part_a(): 
	r""" 
	Write 10,000 pseudorandom numbers drawn from a gaussian to an output file 
	""" 
	with open("problem1.out", 'w') as f: 
		for i in range(int(1e4)): 
			# The %.5f is a float format specifier, w/5-digits after the decimal 
			f.write("%.5f\n" % (np.random.normal())) 
		f.close() 


def part_b(): 
	r""" 
	Read in the 10,000 pseudorandom numbers from part a and ensure that their 
	standard deviation is 1. 
	""" 
	numbers = int(1e4) * [0.] 
	with open("problem1.out", 'r') as f: 
		for i in range(len(numbers)): 
			numbers[i] = float(f.readline()) 
		f.close() 
	print("Standard deviation: %.5f" % (np.std(numbers))) 


if __name__ == "__main__": 
	# this if condition shows up in code a lot - it ensures that you can import 
	# this file without actually running the functions 
	part_a() 
	part_b() 

