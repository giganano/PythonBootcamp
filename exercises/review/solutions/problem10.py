r"""
The solution to problem 10.
"""

def sum_pairs(l):
	r"""
	Add up the integeres which occur multiple times in a given list

	Parameters
	----------
	l : ``list``
		An input ``list`` of integers.

	Returns
	-------
	s : ``int``
		The sum of values which occur more than once in ``l``.
	"""
	# create an empty list to store integers with multiple occurence
	new = []
	for i in l:
		# The ``.count`` function for lists is useful here -- it returns the
		# number of occurences of some object in the list.
		if l.count(i) > 1 and i not in new:
			new.append(i)

	s = 0

	# iterate through the frequency dictionary and add the sum of pairs
	for value in new:
		if value > 1:
			# if the frequency of the integer is greater than 1, calculate the sum of pairs
			s += (value) 

	return s

l = [1, 2, 3, 4, 4, 5, 6, 6, 8, 8, 8, 8]
print(sum_pairs(l))  # Output: 18

