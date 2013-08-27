"""
Problem #5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_evenlydivisible(numerator, range):
	for a in range:
		if numerator % a != 0:
			return False
	return True
	
a = 1
while (not is_evenlydivisible(a, xrange(1, 21))):
	a = a + 1
print a