
# The variable __all__ describes what is imported when the user runs
# from solution.sequences import * 

__all__ = ["primes", "fibonacci"] 
from .primes import prime_generator as primes 
from .fibonacci import print_sequence as fibonacci 
