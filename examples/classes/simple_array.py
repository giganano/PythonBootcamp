r""" 
This is an example of subclassing a built-in. 

See slides for documentation and details on this class. This subclasses list 
to create a simple array. 
""" 


class simple_array(list): 

	def __init__(self, *args, **kwargs): 
		if "dtype" in kwargs.keys(): 
			self._dtype = kwargs["dtype"] 
			del kwargs["dtype"] 
		else: 
			self._dtype = object 

		if all([isinstance(i, self._dtype) for i in args[0]]): 
			super().__init__(*args, **kwargs) 
		else: 
			raise TypeError("All elements must be of the specified data type.") 

	def __setitem__(self, key, value): 
		if isinstance(value, self.dtype): 
			super().__setitem__(key, value) 
		else: 
			raise TypeError("Must be of type %s. Got: %s" % (self.dtype, 
				type(value))) 

	@property 
	def dtype(self): 
		r""" 
		Type : type 

		The data type of the elements. 
		""" 
		return self._dtype 

