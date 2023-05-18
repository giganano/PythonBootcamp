r"""
The solution to problem 8.
"""

def is_palindrome(s):
	r"""
	Determine if a string is a palindrome, neglecting whitespace characters and
	upper-/lower-case letters, and non-alphanumeric characters.

	Parameters
	----------
	s : ``str``
		The input string.

	Returns
	-------
	result : ``bool``
		``True`` if ``s`` is a palindrone, ``False`` if not.

	Notes
	-----
	A string (or integer for that matter) is said to be a palindrome if it is
	equivalent when written in reverse (e.g., "12321").
	"""
	s = s.lower() # Convert all characters to lowercase
	s = ''.join(c for c in s if c.isalnum()) # Remove non-alphanumeric characters
	return s == s[::-1] # Compare the string with its reverse


# Example usage
#
# Here, the input string is set to "was it a car or a cat i saw", which is a
# palindrome. The function returns True, so the program prints "The input
# string is a palindrome.".
#
# Note that this implementation only considers alphanumeric characters when
# checking for palindromes. If you need to consider other characters, you can
# modify the function to include them in the comparison.
input_str = "was it a car or a cat i saw"
if is_palindrome(input_str):
	print("The input string is a palindrome.")
else:
	print("The input string is not a palindrome.")

