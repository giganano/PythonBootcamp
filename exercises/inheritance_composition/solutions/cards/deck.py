r""" 
A part of the solution to the cards problem: A deck of playing cards. 
""" 

from .hand import hand 
from .card import card 
import random 

 
class deck(hand): 

	r""" 
	A deck of cards. Inherits from hand. 

	Parameters 
	----------
	shuffled : bool [default : True] 	
		Whether or not to shuffle the deck immediately. 

	Functions 
	---------
	- shuffle : shuffle the deck 
	- draw : take the card from the top of the deck. 
	""" 

	def __init__(self, shuffled = True): 
		super().__init__(list(range(2, 15)) * 4, 
			13 * ['c'] + 13 * ['d'] + 13 * ['h'] + 13 * ['s']) 
		if shuffled: self.shuffle() 

	def __repr__(self): 
		return super().__repr__().replace("Hand", "Deck") 

	def shuffle(self): 
		r""" 
		Shuffle the deck (i.e. randomize the order of the cards remaining in 
		the deck). 

		Raises 
		------
		* RuntimeError 
			- The deck is empty 
		""" 
		if self.n: 
			random.shuffle(self._cards) 
		else: 
			raise RuntimeError("Deck empty, no cards left!") 

	def draw(self): 
		r""" 
		Take the card in first position and remove it from the deck. 

		Raises 
		------
		* RuntimeError 
			- The deck is empty 
		""" 
		if self.n: 
			x = self.cards[0] 
			del self.cards[0] 
			return x 
		else: 
			raise RuntimeError("Deck empty, no cards left!") 


	@classmethod 
	def fromdeck(cls, drawpile, n): 
		r""" 
		Not supported for this subclass. 
		""" 
		raise TypeError("fromdeck not supported for this subclass.") 


