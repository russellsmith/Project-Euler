
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2    =     0.5
1/3    =     0.(3)
1/4    =     0.25
1/5    =     0.2
1/6    =     0.1(6)
1/7    =     0.(142857)
1/8    =     0.125
1/9    =     0.(1)
1/10    =     0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


    

if __name__ == "__main__":
    numerator, denom = 1, 6
    longest_cycle = -1
    longest_cycle_value = ''
    
    for i in xrange(1,1001,1):
        # Start numerator at 10, for 1.0
        numerator, denom = 10, i

        shifts = []
        quotients = []
        numerators = []
        repeating_pattern = ''
        while True:
            # Keep track of numerator*10 shifts
            shift = 0
            
            # If numerator is 0 this is not a repeating decimal
            if numerator == 0:
                break
            
            # Shift by powers of 10 until we can divide
            while numerator < denom:
                numerator *= 10
                shift += 1
            
            # See if numerator has been processed already, if so we've begun repeating
            if numerator in numerators:
                # Repeating numerator
                # Find index of first occurrence
                index = numerators.index(numerator)
                for j in xrange(index, len(numerators)):
                    # Construct string representation of cycle
                    shift = shifts[j]
                    quotient = quotients[j]
                    num = '0' * shift + str(quotient)
                    repeating_pattern += num
                print('Repeating pattern of length %d for 1/%d is %s'%(len(repeating_pattern), i, repeating_pattern))
                
                break
            
            # Long division
            quotient, remainder = divmod(numerator, denom)
            
            numerators.append(numerator)
            quotients.append(quotient)
            shifts.append(shift)

            numerator = remainder*10
            
        # Keep track of longest cycle
        if len(repeating_pattern) > len(longest_cycle_value):
            longest_cycle = i
            longest_cycle_value = repeating_pattern
    print('Longest cycle is for 1/%d of length %d with pattern %s '%(longest_cycle, len(longest_cycle_value), longest_cycle_value))

