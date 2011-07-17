"""
Problem #9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt

def find_pythagorean_triplet():
	c, sum = 0, 0
	for a in xrange(1, 1001):
		for b in xrange(a + 1, 1001):
			c = sqrt(a * a + b * b)
			sum = a + b + c
			if sum == 1000:
				return a, b, c
				
a, b, c = find_pythagorean_triplet()
print a, b, c
print a * b * c