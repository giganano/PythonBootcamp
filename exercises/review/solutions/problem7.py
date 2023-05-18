r"""
The solution to problem 7.
"""

def print_digits(num):
	r"""
	Prints the digits of a positive integer in order.

	Parameters
	----------
	num : ``int``
		Any integer.

	Notes
	-----
	Function first takes the absolute value of the number, then counts the
	number of digits.
	"""
	if num < 0:
		num *= -1  # convert negative to positive

	# The //= operator is useful in this problem to divide an integer by
	# increasing powers of 10 and taking the quotient, truncating what would be
	# leftover behind the decimal by the /= operator. Recall that ``x //= y``
	# is functionally the same as ``x = x // y``. Note that Python is unique in
	# that true division is the default. In other programming languages, when
	# dividing two integers, the result will behave like the ``//`` operator.
	num_digits = 0
	x = num
	while x > 0:
		num_digits += 1
		x //= 10

	# Extract each digit and print it
	for i in range(num_digits-1, -1, -1):
		digit = num // (10**i)
		print(digit)
		num %= 10**i


print_digits(12345)

# Output 1 2 3 4 5

