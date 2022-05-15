r"""
Implements an object demonstrating that a property of an object is not the
same thing as the data it stores under the hood.
"""

class example:

	def __init__(self, value):
		self._value = value

	@property
	def value(self):
		return self._value

	@property
	def onemore(self):
		return self._value + 1

	@property
	def twomore(self):
		return self._value + 2


