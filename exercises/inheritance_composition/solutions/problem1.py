
from exponential import exponential 
import math as m 

class linear_exponential(exponential): 

	def __call__(self, x): 
		return self.normalization * x * m.exp(-x / self.rate) 
