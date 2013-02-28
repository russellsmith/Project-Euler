"""
Problem #20
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def sum_digits(number):
    sum = 0
    while(number > 0):
        sum += number % 10
        number = number / 10
    return sum

import math
print sum_digits(math.factorial(100))
