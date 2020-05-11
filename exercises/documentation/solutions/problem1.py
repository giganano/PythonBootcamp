r""" 
The solution to problem 1. 
""" 

import matplotlib.pyplot as plt 
import numpy as np 
import math as m 

if __name__ == "__main__": 
	fig = plt.figure() 
	ax = fig.add_subplot(111) 
	ax.set_xlabel("x") 
	ax.set_ylabel("y") 
	ax.set_xlim([0, 2 * m.pi]) 
	ax.set_ylim([-2, 2]) 
	xvals = np.linspace(0, 2 * m.pi, 1000) 
	ax.plot(xvals, 
		[m.sin(i) for i in xvals], 
		c = 'k', # k is black in matplotlib base colors 
		label = "sin") # legend label 
	ax.plot(xvals, 
		[m.cos(i) for i in xvals], 
		c = 'r', # red 
		label = "cos") 
	ax.plot(xvals, 
		[m.tan(i) for i in xvals], 
		c = 'b', 
		label = "tan") 
	ax.legend(loc = 3, frameon = False) 
	plt.savefig("problem1.pdf") 
	plt.savefig("problem1.png") 

