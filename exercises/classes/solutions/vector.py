r""" 
Implements a simple vector object. 

Contents 
--------
- vector : class 
	The class implementing the vector object. 
""" 

import numpy as np 
import numbers 


class vector: 

	r""" 
	N-dimensional vector 

	Parameters 
	----------
	vector : array-like 
		The vector itself as either a list, tuple, or numpy array. 

	Attributes 
	----------
	vector : list 
		The vector itself 
	dimension : int 
		The dimensionality of the vector 

	Indexing 
	--------
	This object can be indexed via integers the same way lists and numpy arrays 
	are indexed - 0 returning the first component, 1 the second, etc. 

	Item Assignment 
	---------------
	Individual components of the vector can be assigned with the same indexing. 

	Example Code 
	------------
	>>> v1 = vector([0, 1, 2]) 
	>>> v2 = vector([1, 2, 3]) 
	>>> v1 + v2 
	<1, 3, 5> 
	>>> v1 * v2 
	<-1, 2, -1> 
	>>> v1 -= v2 
	>>> v1 
	<-1, -1, -1> 
	>>> v1.dot(v2) 
	-6 
	""" 
	def __init__(self, vector): 
		# calls the setter function 
		self.vector = vector 

	@property 
	def vector(self): 
		r""" 
		Type : list 

		The vector itself. 
		""" 
		return self._vector.tolist() 

	@vector.setter 
	def vector(self, value): 
		# Check for lists, tuples, and numpy arrays and just pull a copy 
		if isinstance(value, list) or isinstance(value, tuple): 
			copy = np.array(value[:]) 
		elif isinstance(value, np.ndarray): 
			copy = value[:] 
		else: 
			raise TypeError("""Attribute 'vector' must be initialized from a \
list, tuple, or numpy array. Got: %s""" % (type(value))) 

		# Make sure everything is a number 
		if all([isinstance(i, numbers.Number) for i in copy]): 
			self._vector = copy 
		else: 
			raise TypeError("Non-numerical value in vector.") 

	@property 
	def dimension(self): 
		r""" 
		Type : int 

		The dimensionality of the vector 
		""" 
		return self.__len__() 

	@property 
	def magnitude(self): 
		r""" 
		Type : float 

		The magnitude (or norm) of the vector 
		""" 
		return np.sqrt(self.dot(self)) 

	def __len__(self): 
		r""" 
		Determines the number of components in the vector 
		""" 
		return len(self._vector) 

	def __getitem__(self, key): 
		r""" 
		Returns the i'th component of the vector 
		""" 
		return self._vector[key] 

	def __setitem__(self, key, value): 
		r""" 
		Reassigns the i'th component of the vector 
		""" 
		self._vector[key] = value 

	def __repr__(self): 
		r""" 
		Prints the vector enclosed in brackets <> 
		""" 
		return str(self._vector.tolist()).replace('[', '<').replace(']', '>') 

	def __str__(self): 
		r""" 
		Prints the vector enclosed in brackets <> 
		""" 
		return self.__repr__() 

	def __add__(self, other): 
		r""" 
		Implements vector addition (+ and +=)  
		""" 
		if isinstance(other, vector): 
			if other.dimension == self.dimension: 
				return vector(
					[self[i] + other[i] for i in range(self.dimension)] 
				) 
			else: 
				raise TypeError("Vectors must be of same dimension. Got: %d" % (
					other.dimension)) 
		else: 
			raise TypeError("""Addition only supported with other vectors. \
Got: %s""" % (type(other))) 

	# __radd__ not necessary, __add__ takes care of this already 

	def __sub__(self, other): 
		r""" 
		Implements vector subtraction (- and -=) 
		""" 
		if isinstance(other, vector): 
			if other.dimension == self.dimension: 
				return vector(
					[self[i] - other[i] for i in range(self.dimension)]
				) 
			else: 
				raise TypeError("Vectors must be of same dimension. Got: %d" % (
					other.dimension)) 
		else: 
			raise TypeError("""Subtraction only supported with other vectors. \
Got: %s""" % (type(other))) 

	# __rsub__ not necessary, __sub__ takes care of this already 

	def __mul__(self, other): 
		r""" 
		Implements vector cross products (* and *=) 
		""" 
		if isinstance(other, vector): 
			if other.dimension == self.dimension == 3: 
				new = vector([0, 0, 0]) 
				new[0] = self[1] * other[2] - self[2] * other[1] 
				new[1] = self[2] * other[0] - self[0] * other[2] 
				new[2] = self[0] * other[1] - self[1] * other[0] 
				return new 
			else:
				raise TypeError("Vectors must be of same dimension. Got: %d" % (
					other.dimension)) 
		else: 
			raise TypeError("""Cross product only supported with other \
vectors. Got: %s""" % (type(other))) 

	# __rmul__ not necessary, __mul__ takes care of this already 

	def __eq__(self, other): 
		if isinstance(other, vector): 
			if other.dimension == self.dimension: 
				for i in range(self.dimension): 
					if other[i] != self[i]: return False 
				return True 
			else: 
				return False 
		else: 
			return False 

	def __ne__(self, other): 
		return not self.__eq__(other) 

	def dot(self, other): 
		r""" 
		Evaluate the dot product of this vector with another vector 

		Signature: x.dot(other) 

		Parameters 
		----------
		x : vector 
			The first vector with which to evaluate the dot product. 
		other : vector 
			The second vector with which to evaluate the dot product. 

		Returns 
		------- 
		s : float 
			The sum of the product of each component of the two vectors. 

		Raises 
		------ 
		* TypeError 
			- The two vectors do not have the same dimension. 

		Example Code 
		------------
		>>> v1 = vector([0, 1, 2]) 
		>>> v2 = vector([1, 2, 3]) 
		>>> v1.dot(v2) 
		8 
		>>> v1 *= v2 
		>>> v1.dot(v2) 
		0 
		""" 
		if isinstance(other, vector): 
			if other.dimension == self.dimension: 
				return sum([self[i] * other[i] for i in range(self.dimension)]) 
			else: 
				raise TypeError("Vectors must be of same dimension. Got: %d" % (
					other.dimension)) 
		else: 
			raise TypeError("""Dot product only supported with other vectors. \
Got: %s""" % (type(other))) 

