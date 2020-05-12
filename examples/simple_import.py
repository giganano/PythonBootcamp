r""" 
Run "import simple_import" and also run this file to see what happens 
differently between running and importing a python file. 
""" 

import math as m 
import numbers 


def f(x): 
	r""" 
	Calculate the value of x-squared 
	""" 
	if isinstance(x, numbers.Number): 
		return x**2 
	else: 
		raise TypeError("Must be a numerical value.") 


print("The value of pi squared is %.5f" % (f(m.pi))) 


if __name__ == "__main__": 
	print("The value of e squared is %.5f" % (f(m.e))) 

