
class dog: 

	r""" 
	Implements a dog in python 
	""" 

	def __init__(self, name, breed): 
		self.name = name 
		self.breed = breed 


	@property 
	def name(self): 
		r""" 
		Type : str 

		The name of the dog 
		""" 
		return self._name 


	@name.setter 
	def name(self, value): 
		if isinstance(value, str): 
			self._name = value 
		else: 
			raise TypeError("Attribute 'name' must be a string. Got: %s" % (
				type(value))) 


	@property 
	def breed(self): 
		r""" 
		Type : str 

		The breed of the dog 
		""" 
		return self._breed 

	@breed.setter 
	def breed(self, value): 
		if isinstance(value, str): 
			self._breed = value 
		else: 
			raise TypeError("Attribute 'breed' must be a string. Got: %s" % (
				type(value))) 


