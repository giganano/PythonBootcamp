""" 
Exercise 
======== 
Print a multiplication table for the numbers 1 through 10. Use format 
specifiers in your print statement to make the numbers print with even 
spacing. 
""" 

line = "\t" 
for i in range(1, 11): 
	line += "%d\t" % (i) 
print(line) 
for i in range(1, 11): 
	line = "%d\t" % (i) 
	for j in range(1, 11): 
		line += "%d\t" % (i * j) 
	print(line)  


s = 0
for i in range(len(R)): 
	for j in range(len(theta)): 
		s += (a * T[i][j]**4 * ((R[i] + R[i + 1]) / 2) * 
			(R[i + 1] - R[i]) * 
			(theta[i + 1] - theta[i])) 
