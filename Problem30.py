"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def get_digits(number):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number / 10
        
    return digits

if __name__ == "__main__":
    power = 5
    numbers = []
    for i in xrange(10,1000001,1):
        digits = get_digits(i)
        total = sum([number**power for number in digits])
        if total == i:
            numbers.append(i)
    print ('Sum is %d for %s'%(sum(numbers), numbers))
        
        