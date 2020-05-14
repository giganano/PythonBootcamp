r""" 
The solution to problem 2. 
""" 

import matplotlib.pyplot as plt 
import numpy as np 

def get_bin_number(bins, value): 
	r""" 
	Determine the bin number of a given value given bin edges of a histogram. 

	Parameters 
	----------
	bins : array-like 
		The bin-edges themselves 
	value : float 
		The value to get the bin number of 

	Returns 
	-------
	n : int 
		The bin number of the value. -1 if it does not lie in the range 
		spanned by the bin edges. 
	""" 
	for i in range(len(bins) - 1): 
		if bins[i] <= value <= bins[i + 1]: return i 
	return -1 

if __name__ == "__main__": 
	fig = plt.figure() 
	ax = fig.add_subplot(111) 
	ax.set_xlabel("x") 
	ax.set_ylabel("Counts") 
	ax.set_xlim([-2.5, 2.5]) 

	bins = np.linspace(-2, 2, 11) # 11 bin-edges for 10 bins 
	counts = 10 * [0] 
	for i in range(1000): 
		bin_number = get_bin_number(bins, np.random.normal()) 
		if bin_number != -1: counts[bin_number] += 1 
	ax.step(bins[:-1], counts, c = 'k', where = "post") 
	ax.step(bins[-2:], counts[-2:], c = 'k') 

	centers = 10 * [0] 
	for i in range(len(centers)): 
		centers[i] = (bins[i] + bins[i + 1]) / 2 
	ax.errorbar(centers, counts, yerr = [np.sqrt(i) for i in counts], 
		c = 'k', fmt = 'none') 
	ax.set_ylim([0, ax.get_ylim()[1]]) 

	plt.savefig("problem2.pdf") 
	plt.savefig("problem2.png") 

