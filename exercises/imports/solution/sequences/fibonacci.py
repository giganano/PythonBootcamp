r""" 
The solution to problem 6. 
""" 

import sys 


def fibonacci(n): 
	r""" 
	Generate the first n elements of the Fibonacci Sequence. 

	Parameters 
	----------
	n : int 
		The number of elements of the sequence to generate. 

	Returns 
	-------
	fib : list 
		The first n elements of the Fibonacci Sequence. 

	Raises 
	------
	* ValueError 
		- n < 2 
	""" 
	if isinstance(n, int): 
		if n > 2: 
			fib = n * [0] 
			fib[0] = 0 
			fib[1] = 1 
			for i in range(2, n): 
				fib[i] = fib[i - 2] + fib[i - 1] 
			return fib 
		else: 
			raise ValueError("Must be larger than 2. Got: %d" % (n)) 
	else: 
		raise TypeError("Must be an integer. Got: %s" % (type(n))) 


def print_sequence(n): 
	r""" 
	Print the first n elements of the Fibonacci Sequence. 

	Parameters 
	----------
	n : int 
		The number of elements of the sequence to generate. 

	Raises 
	------
	* ValueError 
		- n < 2 
	""" 
	# Let the fibonacci function do the error handling. 
	for i in fibonacci(n): 
		sys.stdout.write("%d " % (i)) 
	sys.stdout.write("\n") 

	# The following is the one-line solution with a print statement. 
	# print(*fibonacci(n)) 


if __name__ == "__main__": 
	# This if condition shows up in code a lot - it ensures that you can import 
	# this file without actually running the functions 
	print_sequence(int(sys.argv[1])) 

