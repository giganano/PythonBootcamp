r""" 
The solution to problem 5 
""" 

import sys 


def is_prime(n): 
	r""" 
	Determines if the number is prime. 

	Parameters 
	----------
	n : int 
		A potential prime number. 

	Returns 
	-------
	prime : bool 
		True if the number is prime, False otherwise. 

	Raises 
	------
	* ValueError 
		- n is not positive. 
	""" 
	if isinstance(n, int): 
		if n > 2: 
			for i in range(2, n): 
				if n % i == 0: return False 
			return True 
		elif n > 0: 
			return True 
		else: 
			raise ValueError("Must be positive.") 
	else: 
		raise TypeError("Must be an integer. Got: %s" % (type(n))) 


def prime_generator(n): 
	r""" 
	Print the first n prime numbers. 

	Parameters 
	----------
	n : int 
		The number of prime numbers to generate. 

	Raises 
	------
	* ValueError 
		- n is not positive 
	""" 
	if isinstance(n, int): 
		if n > 0: 
			x = 0 
			i = 2 # the smallest prime 
			while x < n: 
				if is_prime(i): 
					print(i) 
					x += 1 
				else: 
					pass # do nothing 
				i += 1 
		else: 
			raise ValueError("Must be positive.") 
	else: 
		raise TypeError("Must be an integer. Got: %s" % (type(n))) 


if __name__ == "__main__": 
	# This if condition shows up in code a lot - it ensures that you can import 
	# this file without actually running the functions 
	prime_generator(int(sys.argv[1])) 

