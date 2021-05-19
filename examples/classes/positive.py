
class positive(int): 

	""" 
	A positive definite integer. 
	""" 

	def __new__(cls, value, *args, **kwargs): 
		if value <= 0: raise ValueError("Must be non-negative and non-zero.") 
		return super().__new__(cls, value, *args, **kwargs) 

	def __add__(self, other): 
		return self.__class__(super().__add__(other)) 

	def __sub__(self, other): 
		return self.__class__(super().__sub__(other)) 

	def __mul__(self, other): 
		return self.__class__(super().__mul__(other)) 

	def __div__(self, other): 
		return self.__class__(super().__div__(other)) 

	def __str__(self): 
		return "%d" % (int(self)) 

	def __repr__(self): 
		return "positive(%d)" % (int(self)) 


