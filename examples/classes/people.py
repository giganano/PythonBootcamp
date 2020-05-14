r""" 
This is an example of inheritance. 

See slides for documentation and details on these classes 
""" 


class person: 

	def __init__(self, name): 
		self.name = name 

	def work(self): 
		r""" 
		Prints a message saying the person is on the clock earning a paycheck. 
		""" 
		print("%s is on the clock earning a paycheck." % (self.name)) 

	@property 
	def name(self): 
		r""" 
		Type : str 

		The person's name. 
		""" 
		return self._name 

	@name.setter 
	def name(self, value): 
		if isinstance(value, str): 
			# Capitalize first letter of their name 
			self._name = value.capitalize() 
		else: 
			raise TypeError("Attribute 'name' must be a string. Got: %s" % (
				type(value))) 


class student(person): 

	def __init__(self, name): 
		super().__init__(name) 

	def work(self): 
		r""" 
		Prints a message saying the student is working on their assignment. 
		""" 
		print("%s is working on the assignment." % (self.name)) 


class professor(person): 

	def __init__(self, name): 
		super().__init__(name) 

	def work(self): 
		r""" 
		Prints a message saying the professor is grading the assignments. 
		""" 
		print("%s is grading the assignments." % (self.name)) 


