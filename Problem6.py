"""
Problem #6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n):
	sum = 0
	for a  in xrange(1, n + 1):
		sum += a * a
	return sum

def square_of_sum(n):
	sum = 0
	for a  in xrange(1, n + 1):
		sum += a
	return sum * sum
	
difference = square_of_sum(100) - sum_of_squares(100)
print difference