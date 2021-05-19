r""" 
A part of the solution to the cards problem: A hand of playing cards. 
""" 

from .card import card 

class hand: 

	r""" 
	A hand of cards. 

	Parameters 
	----------
	values : list 
		Elements are of type int. The face value of each card. 
	suits : list 
		Elements are of type str. The suit identifier of each card. 

	.. seealso:: cards.card 

	Attributes 
	----------
	cards : list 
		The card objects currently in the hand 
	n : int 
		The number of cards in the hand 

	.. note:: This object is indexible and is compatible with the len() 
		function. 

	Functions 
	---------
	- single_draw : draw a single card from a deck 
	- single_discard : discard a single card 
	- fromdeck [classmethod] : Obtain a hand object by drawing from a deck. 
	""" 

	def __init__(self, values, suits): 
		if isinstance(values, list) and isinstance(suits, list): 
			if len(values) == len(suits): 
				self._cards = len(values) * [None] 
				for i in range(len(self._cards)): 
					# Let the card.__init__ function handle errors from here 
					self._cards[i] = card(values[i], suits[i]) 
			else: 
				raise ValueError("Length mismatch. Got: (%d, %d)" % (
					len(values), len(suits))) 
		else: 
			raise TypeError("""Both values and suits must be of type list. \
Got: %s""" % (type(values), type(suits))) 

	def __getitem__(self, idx): 
		return self._cards[idx] 

	def __repr__(self): 
		return ("Hand%s" % (self.cards)).replace('[', '{').replace(']', '}') 

	def __len__(self): 
		return len(self._cards) 

	@property 
	def cards(self): 
		r""" 
		Type : list 

		The cards in the hand. 
		""" 
		return self._cards 

	@property 
	def size(self): 
		r""" 
		Type : int 

		The number of cards in the hand. 
		""" 
		return self.__len__() 

	def single_draw(self, drawpile): 
		r""" 
		Draw from the deck. Adds the card returned from drawpile.draw to the 
		end of the cards attribute. 

		Parameters 
		----------
		drawpile : deck 
			The set of cards to take from 

		Raises 
		------
		* RuntimeError 
			- The drawpile is empty 
		""" 

		# This can't go at the top, because then both files would import one 
		# another and that produces an error 
		from .deck import deck 
		if isinstance(drawpile, deck): 
			self._cards.append(drawpile.draw()) 
		else: 
			raise TypeError("Must be of type deck. Got: %s" % (type(drawpile))) 

	def single_discard(self, discardpile, index): 
		r""" 
		Place a single card in the discard pile 

		Parameters 
		----------
		discardpile : played 
			The played object to give the card to. 
		index : played 
			The index of the card to play in the hand. 

		Raises 
		------
		* IndexError 
			- index is out of bounds 
		""" 
		# This can't go at the top, because then both files would import one 
		# another and that produces an error 
		from .played import played 
		if isinstance(discardpile, played): 
			if isinstance(index, int): 
				# Let list object raise an IndexError for index out of bounds 
				discardpile.add(self._cards[index]) 
				del self._cards[index] 
			else: 
				raise TypeError("'index' must be of type int. Got: %s" % (
					type(index))) 
		else: 
			raise TypeError("'discardpile' must be of type played. Got: %s" % (
				type(discardpile)))  

	@classmethod 
	def fromdeck(cls, drawpile, n): 
		r""" 
		Obtain a hand of cards by drawing a given number from a drawpile 

		Parameters 
		----------
		drawpile : deck 
			The set of cards to take from 
		n : int 
			The number of cards to draw 

		Raises 
		------
		* ValueError 
			- n is not positive 
		""" 

		# This can't go at the top, because then both files would import one 
		# another and that produces an error 
		from .deck import deck 
		if isinstance(drawpile, deck): 
			if isinstance(n, int): 
				if n > 0: 
					hand = cls([], []) 
					for i in range(n): 
						hand.single_draw(drawpile) 
					return hand 
				else: 
					raise ValueError("Must be positive definite. Got: %d" % (n)) 
			else: 
				raise TypeError("'n' must be an integer. Got: %s" % (type(n))) 
		else: 
			raise TypeError("'drawpile' must be a deck. Got: %s" % (
				type(drawpile))) 

