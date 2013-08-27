"""
Problem #5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_evenlydivisible(numerator, range):
	for i in range:
		if numerator % i != 0:
			return False
	return True
	
i = 1
while (not is_evenlydivisible(i, xrange(1, 21))):
	i = i + 1
print i