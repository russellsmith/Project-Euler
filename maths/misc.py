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

if __name__ == "__main__":
    import doctest
    doctest.testmod()