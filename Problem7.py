"""
Problem #7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
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

primeNums = 0
num = 1
while primeNums < 10001:
	num += 1
	if isprime(num):
		primeNums += 1
	
print num