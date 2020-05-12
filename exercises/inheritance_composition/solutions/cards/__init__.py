r""" 
The solution to the playing cards problem 

Contents 
--------
- card : A playing card object 
- hand : A hand of playing cards 
- deck : A deck of playing cards 
- played : A discard pile 

Functions 
--------- 
- card.draw [classmethod] 
- hand.fromdeck [classmethod] 
""" 

__all__ = ["card", "hand", "deck", "played"] 
from .card import card 
from .hand import hand 
from .deck import deck 
from .played import played 
