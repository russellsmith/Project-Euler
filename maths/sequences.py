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