r""" 
The solution to problem 2. 
""" 

import numbers 
import math as m 


class sinusoid: 

	def __init__(self, amplitude = 1, frequency = 1, phase = 0): 
		self.amplitude = amplitude 
		self.frequency = frequency 
		self.phase = phase 

	def __call__(self, x): 
		return self.amplitude * m.sin(self.angular_frequency * x + self.phase) 

	@property 
	def amplitude(self): 
		r""" 
		Type : float 

		The amplitude ofthe sinusoid in arbitrary units 
		""" 
		return self._amplitude 

	@amplitude.setter 
	def amplitude(self, value): 
		if isinstance(value, numbers.Number): 
			if value >= 0: 
				self._amplitude = float(value) 
			else: 
				raise ValueError("Attribute 'amplitude' must be positive.") 
		else: 
			raise TypeError("""Attribute 'amplitude' must be a real number. \
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
			if value > 0: 
				self._frequency = float(value) 
			else: 
				raise ValueError("Attribute 'frequency' must be positive.") 
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
		return 2 * m.pi * self._frequency 

	@angular_frequency.setter 
	def angular_frequency(self, value): 
		# Call the frequency setter and let it do the error handling 
		self.frequency = value / (2 * m.pi) 
