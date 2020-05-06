r""" 
An example package with a small directory tree structure for teaching purposes. 

To import this package, navigate to the directory containing it, then launch 
the python interpreter and import it. Alternatively, place that directory on 
either your PATH or PYTHONPATH, and it can be imported from anywhere 

Contents 
--------
- readdata : Read in a data file of pseudorandomly generated dummy data 
- polynomial : 1-dimenaional polynomial functions of any order 
- sinusoid : Sinusoids of any amplitude, frequency, and phase 
- exponential : Exponential growth/decay with any normalization and scale 
- linearexponential : Linear-exponential functions with any normalization and 
	scale. 
""" 

__all__ = ["readdata"] 
from .readdata import readdata 
from .mathlib import * 
__all__.extend(mathlib.__all__) 

