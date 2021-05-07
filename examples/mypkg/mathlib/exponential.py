r""" 
Implements an exponential growth/decay function 
""" 

import numpy as np 
import numbers 

# This is how you'd access the readdata function in the parent directory 
from ..readdata import readdata 


class exponential: 

	r""" 
	A mathematical exponential growth/decay function given by: 
		f(x) = normalization * exp(x / rate) 

	Parameters 
	----------
	kwargs : real numbers 
		The attributes normalization and rate can be set via keyword 
		arguments. 

	Attributes 
	----------
	normalization : float [default : 1] 
		The value of the exponential at x = 0 
	rate : float [default : 1] 
		The e-folding length in units of the x-coordinate. This is an 
		exponential growth function if this value is positive, and a decay 
		function if negative. 
	""" 

	def __init__(self, normalization = 1, rate = 1): 
		self.normalization = normalization 
		self.rate = rate 

	def __call__(self, x): 
		return self.normalization * np.exp(x / self.rate) 

	def __getitem__(self, key): 
		if key == "normalization": 
			return self._normalization 
		elif key == "rate": 
			return self._rate 
		else: 
			raise KeyError(key) 

	def __setitem__(self, key, value): 
		# call the setter functions for error handling 
		if key == "normalization": 
			self.normalization = value 
		elif key == "rate": 
			self.rate = value 
		else: 
			raise KeyError(key) 

	def __repr__(self): 
		return "%.2fe^(x/%.2f)" % (self.normalization, self.rate) 

	def __str__(self): 
		return self.__repr__() 

	@property 
	def normalization(self): 
		r""" 
		Type : float 

		The value of the exponential at x = 0. 
		""" 
		return self._normalization 

	@normalization.setter 
	def normalization(self, value): 
		if isinstance(value, numbers.Number): 
			self._normalization = float(value) 
		else: 
			raise TypeError("""Attribute 'normalization' must be a real \
number. Got: %s""" % (type(value))) 

	@property 
	def rate(self): 
		r""" 
		Type : float 

		The e-folding length in units of the x-coordinate. This is an 
		exponential growth function if this value is positive, and a decay 
		function if negative. 
		""" 
		return self._rate 

	@rate.setter 
	def rate(self, value): 
		if isinstance(value, numbers.Number): 
			self._rate = float(value) 
		else: 
			raise TypeError("""Attribute 'rate' must be a real number. \
Got: %s""" % (type(value))) 

