"""
Problem #3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def isprime(n):
	n = abs(n)
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i += 1
	return True

target = 600851475143
divisor = 2
while target > 1:
	if target % divisor == 0:
		target = target / divisor
		if(isprime(divisor)):
			largest_prime = divisor
	divisor = divisor + 1
print largest_prime


