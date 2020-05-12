r""" 
A part of the solution to the cards problem: a single playing card. 
""" 

class card: 

	r""" 
	A playing card 

	Parameters 
	----------
	value : int 
		The attribute value. See below. 
	suit : int 
		The attribute suit. See below. 

	Attributes 
	----------
	value : int 
		The face value of the card. 1 for Ace, 11 for Jack, 12 for Queen, and 
		13 for King. 
	suit : str 
		The suit of the card. 'c' for clubs, 'd' for diamonds, 'h' for hearts, 
		and 's' for spades. 
	royal : bool 
		True if the card is royal, False otherwise. 

	.. note:: This class functions with numeric comparison <, <=, ==, !=, >=, 
		and >, returning a comparison of the values of the two cards. 

	Functions 
	---------
	- draw [classmethod] : draw a card from the top of a deck 
	""" 

	def __init__(self, value, suit): 

		# If you wrote setter functions, that would be a sufficient solution 
		# to this problem. However, since a playing card does not have a 
		# modifiable value or suit, it makes sense to not let the user change 
		# them, and therefore to not have setter functions. This requires 
		# error handling in the __init__ function, or some subroutine called 
		# by the __init__ function. 

		# See docstring for value property 
		if isinstance(value, int): 
			if 2 <= value <= 14: 
				self._value = value 
			else: 
				raise ValueError("Value must be between 2 and 14. Got: %d" % (
					value)) 
		else: 
			raise TypeError("Value must be of type int. Got: %s" % (
				type(value))) 
		
		# See docstring for suit property 
		if isinstance(suit, str): 
			if suit in ['c', 'd', 'h', 's']: 
				self._suit = suit 
			else: 
				raise ValueError("Unrecognized suit: %s" % (suit)) 
		else: 
			raise TypeError("Suit must be of type str. Got: %s" % (type(suit))) 

	def __repr__(self): 
		suit = {
			'c': "clubs", 
			'd': "diamonds", 
			'h': "hearts", 
			's': "spades"
		}[self.suit]  
		
		if self.value == 14: 
			value = "Ace" 
		elif self.value == 11: 
			value = "Jack" 
		elif self.value == 12: 
			value = "Queen" 
		elif self.value == 13: 
			value = "King" 
		else: 
			value = self.value 

		return "%s of %s" % (value, suit) 

	# __str__ not needed - returns __repr__ by default 

	def __gt__(self, other): 
		if isinstance(other, card): 
			return self.value > other.value 
		else: 
			raise TypeError("Must be a card. Got: %s" % (type(other))) 

	def __ge__(self, other): 
		if isinstance(other, card): 
			return self.value >= other.value 
		else: 
			raise TypeError("Must be a card. Got: %s" % (type(other))) 


	def __eq__(self, other): 
		if isinstance(other, card): 
			return self.value == other.value 
		else: 
			raise TypeError("Must be a card. Got: %s" % (type(other))) 

	def __le__(self, other): 
		if isinstance(other, card): 
			return self.value <= other.value 
		else: 
			raise TypeError("Must be a card. Got: %s" % (type(other))) 


	def __lt__(self, other): 
		if isinstance(other, card): 
			return self.value < other.value 
		else: 
			raise TypeError("Must be a card. Got: %s" % (type(other))) 

	@property 
	def value(self): 
		r""" 
		Type : int 

		The value of the card. This will be 1 for Ace, 11 for Jack, 12 for 
		Queen, 13 for King, and the face value for the remaining cards. 
		""" 
		return self._value 

	@property 
	def suit(self): 
		r""" 
		Type : str 

		The suit of the card. This will be 'c' for clubs, 'd' for diamonds, 
		'h' for hearts, and 's' for spades. 
		""" 
		return self._suit 

	@property 
	def royal(self): 
		r""" 
		Type : bool 

		True if the card is a royal, False otherwise 
		""" 
		return self.value >= 10 or self.value == 1 

	@classmethod 
	def draw(cls, drawpile): 
		r""" 
		Draw a card from the drawpile. 

		Parameters 
		----------
		drawpile : deck 
			The deck object to draw from. 

		Raises 
		------
		* RuntimeError 
			- The drawpile is empty 
		""" 

		# This can't go at the top, because then both files would import one 
		# another and that produces an error 
		from .deck import deck 
		if isinstance(drawpile, deck): 
			return drawpile.draw() 
		else: 
			raise TypeError("Must be of type deck. Got: %s" % (type(drawpile))) 

