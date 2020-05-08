
# Your solution should have 'pkg' in place of 'solution' here. This simply 
# reflects the different names of the directories. 

import solution 
print("10! = %d" % (solution.factorial(10))) 
print("1 + 2 + 3 + ... + 50 = %d" % (solution.recursive_sum(list(range(51))))) 
print("The first 20 elements of the fibonacci sequence:") 
solution.sequences.fibonacci(20) 
print("The first 20 prime numbers:") 
solution.sequences.primes(20) 
