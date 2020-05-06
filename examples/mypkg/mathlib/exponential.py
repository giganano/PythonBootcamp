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
		f(x) = normalization * exp(x / scale) 

	Parameters 
	----------
	kwargs : real numbers 
		The attributes normalization and scale can be set via keyword 
		arguments. 

	Attributes 
	----------
	normalization : float [default : 1] 
		The value of the exponential at x = 0 
	scale : float [default : 1] 
		The e-folding length in units of the x-coordinate. This is an 
		exponential growth function if this value is positive, and a decay 
		function if negative. 
	""" 

	def __init__(self, normalization = 1, scale = 1): 
		self.normalization = normalization 
		self.scale = scale 

	def __call__(self, x): 
		return self.normalization * np.exp(x / self.scale) 

	def __repr__(self): 
		return "%.2fe^(x/%.2f)" % (self.normalization, self.scale) 

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
			self._normalization = value 
		else: 
			raise TypeError("""Attribute 'normalization' must be a real \
number. Got: %s""" % (type(value))) 

	@property 
	def scale(self): 
		r""" 
		Type : float 

		The e-folding length in units of the x-coordinate. This is an 
		exponential growth function if this value is positive, and a decay 
		function if negative. 
		""" 
		return self._scale 

	@scale.setter 
	def scale(self, value): 
		if isinstance(value, numbers.Number): 
			self._scale = value 
		else: 
			raise TypeError("""Attribute 'scale' must be a real number. \
Got: %s""" % (type(value))) 

