"""
Problem #10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def isprime(n):
	n *= 1.0
	if n % 2 == 0 and n != 2:
		# Any number divisible by 2 is not prime, unless it is 2
		return False
	for divisor in xrange(3, int(n ** 0.5) + 1, 2):
		if n % divisor == 0:
			return False
	return True
	
def sumprimes(n):
	sum = 0
	for a in xrange(2, n):
		if isprime(a):
			sum += a
	return sum
	
print sumprimes(2000000)