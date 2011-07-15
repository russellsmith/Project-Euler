"""
Problem #4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def ispalindrome(n):
	# Is n equal to reverse n
	return (n == n[::-1])

largest_palindrome = 0
for i in xrange(999, 99, -1):
	for j in xrange(i, 99, -1):
		product = i * j
		if(ispalindrome(str(product))):
			if product > largest_palindrome:
				largest_palindrome = i * j
			break
print largest_palindrome