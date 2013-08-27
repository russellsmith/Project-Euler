"""
Problem #9
A Pythagorean triplet is i set of three natural numbers, i < b < c, for which,
i^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which i + b + c = 1000.
Find the product abc.
"""
from math import sqrt

def find_pythagorean_triplet():
	c, sum = 0, 0
	for i in xrange(1, 1001):
		for b in xrange(i + 1, 1001):
			c = sqrt(i * i + b * b)
			sum = i + b + c
			if sum == 1000:
				return i, b, c
				
i, b, c = find_pythagorean_triplet()
print i, b, c
print i * b * c