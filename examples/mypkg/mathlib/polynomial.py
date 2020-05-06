r""" 
Implements a polynomial callable object 
""" 

import numpy as np 
import numbers 

# This is how you'd access the readdata function in the parent directory 
from ..readdata import readdata 


class polynomial: 

	r""" 
	N-th degree mathematical polynomial functions f(x) 

	Parameters 
	----------
	coeffs : array-like 
		The coefficients of the polynomial. See attribute below. 
		Must be either a list, tuple, or numpy array. 

	Attributes 
	----------
	coeffs : numpy array 
		The coefficients of the polynomial, in order of increasing exponent on 
		the independent variable x. 
	order : int 
		The order of the polynomial. 
	""" 

	def __init__(self, coeffs): 
		self.coeffs = coeffs 

	def __getitem__(self, index): 
		if isinstance(index, numbers.Number) and index % 1 == 0: 
			return self._coeffs[index] 
		else: 
			raise IndexError("Index must be an integer.") 

	def __call__(self, x): 
		result = 0 
		for i in range(len(self._coeffs)): 
			result += x**i * self._coeffs[i] 
		return result 

	def __repr__(self): 
		rep = "" 
		for i in range(self.order + 1): 
			if i: 
				if self._coeffs[i] > 0: 
					rep += "+ %.2fx^%d " % (self._coeffs[i], i) 
				elif self._coeffs[i] < 0: 
					rep += "- %.2fx^%d " % (self._coeffs[i], i) 
				else: 
					# don't print if the coefficient is zero 
					pass 
			else: 
				if self._coeffs[i] > 0: 
					rep += "%.2f " % (self._coeffs[i]) 
				elif self._coeffs[i] < 0: 
					rep += "-%.2f " % (self._coeffs[i]) 
				else: 
					# don't print if the coefficient is zero 
					pass 
		return rep 

	def __str__(self): 
		return self.__repr__() 

	@property 
	def coeffs(self): 
		r""" 
		Type : numpy array 

		The numerical coefficients of the polynomial, in order of increasing 
		exponent on x 
		""" 
		return self._coeffs 

	@coeffs.setter 
	def coeffs(self, value): 
		if isinstance(value, list) or isinstance(value, tuple): 
			if all([isinstance(i, numbers.Number) for i in value]): 
				self._coeffs = np.array(value) 
			else: 
				raise TypeError("Non-numerical value in coefficients.") 
		elif isinstance(value, np.ndarray): 
			if all([isinstance(i, numbers.Number) for i in value]): 
				self._coeffs = value[:] 
			else: 
				raise TypeError("Non-numerical value in coefficients.") 
		else: 
			raise TypeError("""Attribute 'coeffs' must be either a list, \
tuple, or numpy array. Got: %s""" % (type(value))) 

	@property 
	def order(self): 
		r""" 
		Type : int 

		The order of the polynomial 
		""" 
		return len(self._coeffs) - 1 

