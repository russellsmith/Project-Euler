"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
if __name__ == "__main__":
    from maths.misc import get_digits
    from math import factorial
    # Pre compute factorials from 0-9
    factorials = dict((i, factorial(i)) for i in xrange(0,10))
    result = []
    
    # Trial and error on the upper bound.
    for i in xrange(10,100000):
        # Get digits in number
        digits = get_digits(i)
        factorial_sum = 0
        # Sum factorial of the digits
        for digit in digits:
            factorial_sum += factorials[digit]
        # Sum matches our condition
        if factorial_sum == i:
            result.append(i)
    print sum(result)