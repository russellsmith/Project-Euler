def triangle_numbers(limit = None):
    triangle_sum = 0
    
    if limit is None:
        # Infinite sequence
        import itertools
        for a in itertools.count(1, 1):
            triangle_sum += a
            yield triangle_sum, a
        
    else:
        # Finite sequence
        for a in xrange(1, limit, 1):
            triangle_sum += a
            yield triangle_sum, a