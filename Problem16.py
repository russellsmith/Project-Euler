"""
Problem #16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sumdigits(n):
	numString = str(n)
	sum = 0
	for char in numString:
		sum += int(char)
	return sum
	
number = 2 ** 1000
sum = sumdigits(number)
print "The sum of", str(number), "is", str(sum)