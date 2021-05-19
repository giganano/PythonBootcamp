
from exponential import exponential 

class linear_exponential(exponential): 

	def __call__(self, x): 
		return x * super().__call__(x) 
