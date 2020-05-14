r""" 
The solution to problem 1. 
""" 

import numbers 
import math as m 


class exponential: 

	def __init__(self, normalization = 1, rate = 1): 
		self.normalization = normalization 
		self.rate = rate 

	def __call__(self, x): 
		return self.normalization * m.exp(x / self.rate) 

	@property 
	def normalization(self): 
		r""" 
		Type : float 

		The value of the exponential at x = 0 
		""" 
		return self._normalization 

	@normalization.setter 
	def normalization(self, value): 
		if isinstance(value, numbers.Number): 
			self._normalization = value 
		else: 
			raise TypeError("""Attribute 'normalization' must be a real \
number. Got: %s""" % (type(value))) 

	@property 
	def rate(self): 
		r""" 
		Type : float 

		The e-folding length of the exponential in the same units as the 
		x-coordinate. For positive scales, this is an exponential growth, and 
		an exponential decay for negative scales. 
		""" 
		return self._rate 

	@rate.setter 
	def rate(self, value): 
		if isinstance(value, numbers.Number): 
			self._rate = value 
		else: 
			raise TypeError("Attribute 'rate' must be a real number. Got: %s" % (
				type(value))) 

