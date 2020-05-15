r""" 
The solution to problem 3. 
""" 

class pet: 

	def __init__(self, name): 
		self.name = name 

	@property 
	def name(self): 
		r""" 
		Type : str 

		The name of your pet. 
		""" 
		return self._name 

	@name.setter 
	def name(self, value): 
		if isinstance(value, str): 
			# Capitalize their name 
			self._name = value.capitalize() 
		else: 
			raise TypeError("Attribute 'name' must be a string. Got: %s" % (
				type(value))) 


class cat(pet): 

	def meow(self): 
		r""" 
		The cat says "Meow!" 
		""" 
		print("Meow!") 

	def play(self): 
		r""" 
		Chases the laser pointer. 
		""" 
		print("%s is chasing the laser pointer!" % (self.name)) 


class dog(pet): 

	def bark(self): 
		r""" 
		The dog says "Woof!" 
		""" 
		print("Woof!") 

	def play(self): 
		r""" 
		The dog plays fetch. 
		""" 
		print("%s is playing fetch!" % (self.name)) 


