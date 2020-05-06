r""" 
Implements a linear-exponential function 
""" 

# This has only one dot, because it's in this directory 
from .exponential import exponential 
import numpy as np 

# This is how you'd access the readdata function in the parent directory 
from ..readdata import readdata 


class linearexponential(exponential): 

	r""" 
	A mathematical linear-exponential function given by: 
		f(x) = normalization * x * exp(-x / scale) 

	Parameters 
	----------
	kwargs : real numbers 
		The attributes normalization and scale can be set via keyword 
		arguments. 

	Attributes 
	----------
	normalization : float [default : 1] 
		The value of the exponential at x = 0 
	scale : float [default : 1] 
		The e-folding length in units of the x-coordinate. This will only have 
		the characteristic linear-exponential turnover behavior if this 
		value is positive. 
	""" 

	def __init__(self, **kwargs): 
		# let super handle the errors 
		super().__init__(**kwargs) 

	def __call__(self, x): 
		return self.normalization * x * np.exp(-x / self.scale) 

	def __repr__(self): 
		return "%.2fxe^(-x/%.2f)" % (self.normalization, self.scale) 

