"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a d.n.e. b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


if __name__ == "__main__":
    from maths.misc import find_divisors
    amicable_numbers = {}
    
    for a in xrange(1, 10001, 1):
        if a not in amicable_numbers:
            proper_divisors_a = list(find_divisors(a, True))
            
            divisor_sum_a = sum(proper_divisors_a)
            
            # Ensure that d(a) != a
            if divisor_sum_a == a:
                continue
            
            proper_divisors_b = list(find_divisors(divisor_sum_a, True))
            
            divisor_sum_b = sum(proper_divisors_b)
            if divisor_sum_b == a:
                amicable_numbers[a] = divisor_sum_a
                amicable_numbers[divisor_sum_a] = a
    
    numbers = [nums[1] for nums in amicable_numbers.items()]
    total = sum(numbers)
#         
    print 'Total sum is %d'%total
    