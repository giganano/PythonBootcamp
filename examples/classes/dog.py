
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


	def speak(self): 
		r""" 
		Makes the dog bark when you tell it to speak. 
		""" 
		print("%s says \"Woof!\"" % (self.name))   


	@staticmethod 
	def is_puppy(age): 
		r""" 
		Determine if a dog is a puppy. 

		Signature: dog.is_puppy(age) 

		Parameters 
		----------
		age : int 
			The age of the dog, in years 

		Returns 
		-------
		puppy : bool 
			True if age < 2 years, otherwise False. 
		""" 
		if isinstance(age, int): 
			return age < 2 
		else: 
			raise TypeError("Must be an integer. Got: %s" % (type(age))) 


	@classmethod 
	def snoopy(cls): 
		r""" 
		Returns Snoopy. 
		""" 
		return cls("Snoopy", "Beagle") 


