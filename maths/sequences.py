def triangle_numbers(limit = None):
    triangle_sum = 0
    
    if limit is None:
        # Infinite sequence
        import itertools
        for i in itertools.count(1, 1):
            triangle_sum += i
            yield triangle_sum, i
        
    else:
        # Finite sequence
        for i in xrange(1, limit, 1):
            triangle_sum += i
            yield triangle_sum, i
            
def abundant_numbers(limit=None):
    from maths.misc import find_divisors
    if limit is None:
        # Infinite sequence
        import itertools
        for i in itertools.count(1,1):
            divisors = find_divisors(i, True)
            if sum(divisors) > i:
                yield i
    
    else:
        # Finite sequence
        for i in xrange(1, limit, 1):
            divisors = find_divisors(i, True)
            if sum(divisors) > i:
                yield i
                
def fibonacci():
    import itertools
    prev, current, fib, iteration = 0, 1, 1, 1
    for i in itertools.count(1,1):
        yield fib, iteration
        fib = prev + current
        prev, current, iteration = current, fib, iteration + 1 

def prime_numbers(**kwargs):
    from maths.misc import is_prime
    limit = kwargs.get('limit', None)
    start = kwargs.get('start', 1)
    if limit is None:
        import itertools
        for i in itertools.count(start,1):
            if is_prime(i):
                yield i
                
    else: 
        found_primes = 0
        i = start
        while found_primes < limit:
            if is_prime(i):
                found_primes += 1
                yield i
            i += 1
    