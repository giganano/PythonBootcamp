r""" 
The solution to problem 4. 
""" 

import numpy as np 
import numbers 


def recursive_sum(arr): 
	r""" 
	Calculate the sum of an array of numbers using recursion. 

	Parameters 
	----------
	arr : array-like 
		The array to sum 

	Returns 
	-------
	s : float 
		The sum of the array 

	Raises 
	------
	* TypeError 
		- arr contains a non-numerical value. 
	""" 
	if (isinstance(arr, list) or 
		isinstance(arr, tuple) or 
		isinstance(arr, np.ndarray)): 
		if all([isinstance(i, numbers.Number) for i in arr]): 
			if len(arr): 
				return arr[0] + recursive_sum(arr[1:]) 
			else: 
				return 0 
		else: 
			raise TypeError("Non-numerical value in array.") 
	else: 
		raise TypeError("Must be array-like. Got: %s" % (type(arr))) 


def part_b(): 
	r""" 
	The solution to part d 
	""" 
	for i in range(50): print(recursive_sum(list(range(1, i + 2)))) 


if __name__ == "__main__": 
	# this if condition shows up in code a lot - it ensures that you can import 
	# this file without actually running the functions 
	part_b() 

