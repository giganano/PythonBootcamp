r""" 
Implements a reader of the data file mypkg/mydata/somedata.dat 
""" 

import numpy as np 
import os 


def readdata(): 
	r""" 
	Reads in the data file at mypkg/mydata/somedata.dat 
	""" 
	# full path to this file can be accessed via __file__ 
	return np.genfromtxt("%s/mydata/somedata.dat" % (
		os.path.dirname(os.path.abspath(__file__)))) 

