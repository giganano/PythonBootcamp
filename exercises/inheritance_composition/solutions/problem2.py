
class ci_dict(dict): 

	def __init__(self, **kwargs): 
		copy = {} 
		for i in kwargs.keys(): 
			# the keys of **kwargs will always be strings 
			copy[i.lower()] = kwargs[i] 
		super().__init__(**kwargs) 

	def __getitem__(self, key): 
		if isinstance(key, str): 
			return super().__getitem__(key.lower()) 
		else: 
			return super().__getitem__(key) 

	def __setitem__(self, key, value): 
		if isinstance(key, str): 
			super().__setitem__(key.lower(), value) 
		else: 
			super().__setitem__(key, value) 

