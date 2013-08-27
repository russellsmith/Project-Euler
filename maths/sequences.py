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