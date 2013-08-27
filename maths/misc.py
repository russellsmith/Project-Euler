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

if __name__ == "__main__":
    import doctest
    doctest.testmod()