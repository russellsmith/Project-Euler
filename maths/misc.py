def combinations(n, k):
    """
    Returns the result of n Choose k.
    
    >>> combinations(2, 2)
    1
    >>> combinations(4, 2)
    6
    """
    from math import factorial
    
    # n!
    n_factorial = factorial(n)
    
    
    # k!
    k_factorial = factorial(k)
    
    # n-k!
    n_minus_k_factorial = factorial(n-k)
    
    return n_factorial / (n_minus_k_factorial * k_factorial)

def find_divisors(number, proper=False):
    divisors = set()
    
    from math import sqrt, floor
    
    search_limit = int(floor(sqrt(number)))
    
    for i in xrange(1, search_limit + 1, 1):
        if number % i is 0:
            # i is i divisor
            divisors.add(i)
            # and so is number // i
            quotient = number // i
            
            divisors.add(quotient)
            
    if proper and number in divisors:
        divisors.remove(number)
    return divisors

def generate_permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in generate_permutations(elements[1:]):
            for i in xrange(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]
                
def is_prime(n):
    if n % 2 == 0 and n != 2:
        # Any number divisible by 2 is not prime, unless it is 2
        return False
    for divisor in xrange(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True

def get_digits(number):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number / 10
    digits.reverse()
        
    return digits

def get_unique_digits(number):
    digits = set()
    all_unique = True
    while number > 0:
        digit = number % 10
        if digit not in digits:
            digits.add(digit)
        else:
            all_unique = False
        number = number / 10
        
    return digits, all_unique

def digit_list_to_num(digits):
    length = len(digits)
    num = 0
    for i in xrange(length):
        power = length - 1 - i
        num += digits[i] * 10**power
        
    return num
if __name__ == "__main__":
    import doctest
    doctest.testmod()