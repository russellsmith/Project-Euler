"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
def shift_digits(digits, offset):
    return digits[offset:] + digits[:offset]

def list_to_num(digits):
    length = len(digits)
    num = 0
    for i in xrange(length):
        power = length - 1 - i
        num += digits[i] * 10**power
        
    return num

if __name__ == "__main__":
    from maths.misc import get_digits, is_prime
    
    circular_primes = []
    
    for i in xrange(2, 1000000):
        if not is_prime(i):
            continue
        prime = True
        digits = get_digits(i)
        for offset in xrange(1,len(digits)):
            shifted = shift_digits(digits, offset)

            num = list_to_num(shifted)
            
            if not is_prime(num):
                prime = False
                break
        if prime:
            circular_primes.append(i)
    print('The number of circular primes below 1,000,000 is %d'%len(circular_primes))