r""" 
A part of the solution to the cards problem: A discard pile. 
""" 

from .hand import hand 
from .card import card 


class played(hand): 

	r""" 
	A discard pile. Inherits from hand. 

	Functions 
	---------
	- add : add a card to the discard pile. 
	""" 

	def __init__(self): 
		super().__init__([], []) 

	def __repr__(self): 
		return super().__repr__().replace("Hand", "DiscardPile") 

	def add(self, discard): 
		r""" 
		Add a card to the discard pile. 

		Parameters 
		----------
		discard : card 
			The card to add to the discard pile. 
		""" 
		if isinstance(discard, card): 
			self._cards.append(discard) 
		else: 
			raise TypeError("Must be a card. Got: %s" % (type(discard))) 

	def single_discard(self, discardpile, index): 
		r""" 
		Not supported for this subclass. 
		""" 
		raise TypeError("single_discard not supported for this subclass.") 

	@classmethod 
	def fromdeck(cls, drawpile, n): 
		r""" 
		Not supported for this subclass. 
		""" 
		raise TypeError("fromdeck not supported for this subclass.") 

