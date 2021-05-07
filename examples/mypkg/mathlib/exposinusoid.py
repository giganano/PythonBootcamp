""" 
Implements a piece-wise exponential-sinusoid object. 
""" 

# import the necessary pieces 
from .exponential import exponential 
from .sinusoid import sinusoid 


class exposinusoid(exponential, sinusoid): 

	r""" 
	A mathematical function which is a sinusoid for x < 0 but an exponential 
	for x >= 0. 

	Parameters 
	----------
	kwargs : real numbers 
		The attributes of the ``exponential`` and ``sinusoid`` classes. 

	Attributes are inherited from the ``exponential`` and ``sinusoid`` 
	classes. 
	""" 

	def __init__(self, amplitude = 1, frequency = 1, phase = 0, 
		normalization = 1, rate = 1): 

		exponential.__init__(self, normalization = normalization, rate = rate) 
		sinusoid.__init__(self, amplitude = amplitude, frequency = frequency, 
			phase = phase) 

	def __call__(self, x): 
		if x >= 0: 
			return exponential.__call__(self, x) 
		else: 
			return sinusoid.__call__(self, x) 

