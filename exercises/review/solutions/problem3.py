r""" 
The solution to problem 3. 
""" 

def factorial(n): 
	r""" 
	Calculate the value of n! 

	Parameters 
	----------
	n : int 
		The number to calculate the factorial of. 

	Returns 
	-------
	x : int 
		The value of n!. 

	Raises 
	------
	* ValueError 
		- n < 0 
	""" 
	if n < 0: 
		raise ValueError("n must be positive.") 
	elif n: 
		# recall that numbers can be used in if/else statements too 
		return n * factorial(n - 1) 
	else: 
		return 1 


def part_b(): 
	r""" 
	The solution to part b
	""" 
	for i in range(50): print("%d! = %d" % (i + 1, factorial(i + 1))) 



if __name__ == "__main__": 
	# this if condition shows up in code a lot - it ensures that you can import 
	# this file without actually running the functions 
	part_b() 

