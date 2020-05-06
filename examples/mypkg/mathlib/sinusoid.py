r""" 
Implements a sinusoid callable object 
""" 

import numpy as np 
import numbers 

# This is how you'd access the readdata function in the parent directory 
from ..readdata import readdata 


class sinusoid: 

	r""" 
	A mathematical sinusoid given by: 
		f(x) = amplitude * sin(2 * pi * frequency * x + phase) 

	Parameters 
	---------- 
	kwargs : real numbers 
		The attributes amplitude, frequency, and phase can be initialize via 
		keyword arguments. 

	Attributes 
	----------
	amplitude : float [default : 1] 
		The amplitude of the sinusoid in arbitrary units. 
	frequency : float [default : 1] 
		The frequency of the sinusoid in units of the inverse x-coordinate. 
	phase : float [default : 0] 
		The phase of the sinusoid in units of the x-coordinate.
	""" 

	def __init__(self, amplitude = 1, frequency = 1, phase = 0): 
		self.amplitude = amplitude 
		self.frequency = frequency 
		self.phase = phase 

	def __call__(self, x): 
		return self.amplitude * np.sin(2 * np.pi * self.frequency * x + 
			self.phase) 

	def __repr__(self): 
		return "%.2fsin(2pi(%.2f)x + %.2f)" % (
			self.amplitude, 
			self.frequency, 
			self.phase 
		) 

	def __str__(self):  
		return self.__repr__() 

	@property 
	def amplitude(self): 
		r""" 
		Type : float 

		The amplitude of the sinusoid in arbitrary units 
		""" 
		return self._amplitude 

	@amplitude.setter 
	def amplitude(self, value): 
		if isinstance(value, numbers.Number): 
			self._amplitude = float(value) 
		else: 
			raise TypeError("""Attribute 'amplitude' must be real number. \
Got: %s""" % (type(value))) 

	@property 
	def frequency(self): 
		r""" 
		Type : float 

		The frequency of the sinusoid in units of the inverse x-coordinate. 
		""" 
		return self._frequency 

	@frequency.setter 
	def frequency(self, value): 
		if isinstance(value, numbers.Number): 
			self._frequency = float(value) 
		else: 
			raise TypeError("""Attribute 'frequency' must be a real number. \
Got: %s""" % (type(value))) 

	@property 
	def phase(self): 
		r""" 
		Type : float 

		The phase of the sinusoid in units of the x-coordinate. 
		""" 
		return self._phase 

	@phase.setter 
	def phase(self, value): 
		if isinstance(value, numbers.Number): 
			self._phase = float(value) 
		else: 
			raise TypeError("""Attribute 'phase' must be a real number. \
Got: %s""" % (type(value))) 

	@property 
	def angular_frequency(self): 
		r""" 
		Type : float 

		The angular frequency of the sinusoid in units of the inverse 
		x-coordinate. 
		""" 
		return 2 * np.pi * self._frequency 

