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
		if isinstance(index, int): 
			# Don't need any more error handling - self._coeffs is a numpy 
			# array and will raise errors for us 
			return self._coeffs[index] 
		else: 
			raise IndexError("Index must be an integer.") 

	def __call__(self, x): 
		result = 0 
		for i in range(len(self._coeffs)): 
			result += x**i * self._coeffs[i] 
		return result 

	def __setitem__(self, index, value): 
		if isinstance(index, int): 
			if 0 <= index <= self.order: 
				if isinstance(value, numbers.Number): 
					self._coeffs[index] = value 
				else: 
					raise TypeError("Must be a numerical value. Got: %s" % (
						type(value))) 
			else: 
				raise IndexError("Index out of bounds.") 
		else: 
			raise IndexError("Must be an integer. Got: %s" % (type(index))) 

	def __repr__(self): 
		rep = "" 
		for i in range(self.order + 1): 
			if i: 
				if self._coeffs[i] > 0: 
					rep += "+ %.2fx^%d " % (self._coeffs[i], i) 
				elif self._coeffs[i] < 0: 
					rep += "- %.2fx^%d " % (-self._coeffs[i], i) 
				else: 
					# don't print if the coefficient is zero 
					pass 
			else: 
				if self._coeffs[i] > 0: 
					rep += "%.2f " % (self._coeffs[i]) 
				elif self._coeffs[i] < 0: 
					rep += "-%.2f " % (-self._coeffs[i]) 
				else: 
					# don't print if the coefficient is zero 
					pass 
		return rep 

	def __str__(self): 
		return self.__repr__() 

	def __pos__(self): 
		return self 

	def __neg__(self): 
		return polynomial([-i for i in self._coeffs]) 

	def __add__(self, other): 
		if isinstance(other, polynomial): 
			new_coeffs = (max(other.order, self.order) + 1) * [0.] 
			for i in range(len(new_coeffs)): 
				if i <= self.order: new_coeffs[i] += self[i] 
				if i <= other.order: new_coeffs[i] += other[i] 
			return polynomial(new_coeffs) 
		else: 
			raise TypeError("Must be a polynomial object. Got: %s" % (
				type(other))) 

	def __sub__(self, other): 
		if isinstance(other, polynomial): 
			# The same as "return self + -other" 
			return self.__add__(other.__neg__()) 
		else: 
			raise TypeError("Must be a polynomial object. Got: %s" % (
				type(other))) 

	def __eq__(self, other): 
		if isinstance(other, polynomial): 
			if self.order == other.order: 
				# The numpy array does component-wise comparison here, hence 
				# the usage of all 
				return all(self.coeffs == other.coeffs) 
			else: 
				return False 
		else: 
			return False 

	def __ne__(self, other): 
		return not self.__eq__(other) 

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

