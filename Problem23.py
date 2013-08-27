"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
if __name__ == "__main__":
    from maths.sequences import abundant_numbers
    
    limit = 28123
    number_set = set()
    
    # Create a set of abundant numbers up to 28123
    for num in abundant_numbers(limit):
        number_set.add(num)
    
    # Convert set to list and sort it
    number_list = list(number_set)
    number_list.sort()
    
    results = []
    
    for target in xrange(1, limit, 1):
        can_be_summed = False
        for j in xrange(0, len(number_list), 1):
            number = number_list[j]
            
            # No point in continuing to check if number is greater than our target
            if number > target:
                break
            
            # Find the difference between target and abundant number
            difference = target - number
            
            # Check to see if difference is in set of abundant numbers
            if difference in number_set:
                can_be_summed = True
                break
        
        if not can_be_summed:
            results.append(target)
        
    print 'Resulting sum is %d' % sum(results)