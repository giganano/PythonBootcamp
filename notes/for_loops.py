""" 
For-Loops 
========= 
This script is an example of both implicit and explicit for loops. 

Loops, in general, repeat a piece of code some number of times. A for loop 
should be used when the developer knows exactly how many times the 
operation should repeat itself. 

For loops come in two different types: implicit and explicit. An imlicit for 
loop takes place inside a list comprehension, and thus can only be used in the 
creation or modification of array-like objects. An explicit for loop wraps a 
block of indented text which can be as long and complex as necessary. 

Stylistic Notes 
=============== 
Long and convoluted for loops are considered bad style. As a rule of thumb, 
if a for-loop exceeds ~10-15 lines, there is likely a more efficient approach 
to the problem. 
""" 


""" 
Imlicit for loops take place inside brackets to create lists or parentheses 
to create tuples. 
""" 
print("These are examples of implicit for loops:") 
print([i for i in range(10)]) 
print([i**2 for i in range(10)]) 
print([i**2 + 3 * i - 4 for i in range(10)]) 


""" 
Explicit for loops can be used to create the same lists 
""" 
print("These are examples of simple explicit for loops:") 
x = 10 * [0] 
for i in range(10): 
	x[i] = i 
print(x) 
for i in range(10): 
	x[i] = i**2 
print(x) 
for i in range(10): 
	x[i] = i**2 + 3 * i - 4 
print(x) 


""" 
Explicit for-loops, however, can be much more complicated. 
""" 
print("This is an explicit for-loop which calculates x! for 1 through 10.") 
for i in range(1, 11): 
	product = 1 
	for j in range(1, i + 1): 
		product *= j
	print(i, "! = ", product) 

