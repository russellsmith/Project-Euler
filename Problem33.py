"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def reduce_fraction(num, denom):
    from maths.misc import find_divisors
    # Find divisors of num & denom
    proper_divisors = True
    div_n = find_divisors(num, proper_divisors)
    div_d = find_divisors(denom, proper_divisors)
    
    # Find intersection between divisors of numerator and denominator
    intersection = list(div_n.intersection(div_d))
    
    # Sort descending
    intersection.sort()
    intersection.reverse()
    
    for i in intersection:
        # Check that num and denom are still evenly divisible by i
        # Need to check this as we're not only reducing by prime numbers
        # We don't want to "over-reduce"
        if num % i == 0 and denom % i == 0:
            num = num / i
            denom = denom / i 
    return num, denom
    

if __name__ == "__main__":
    from maths.misc import get_digits
    numerators = []
    denominators = []
    
    for i in xrange(10,100):
        for j in xrange(i + 1,100):
            # Get digits of i,j
            digits_i, digits_j = get_digits(i), get_digits(j)
            
            # Check for overlap
            overlap = filter(set(digits_i).__contains__, digits_j)
            
            if len(overlap) > 0:
                # Pull first char from overlap
                char_to_remove = overlap[0]
                
                # Check for trivial case where digits to be removed are in the same power of 10s position
                index_i = digits_i.index(char_to_remove)
                index_j = digits_j.index(char_to_remove)
                if index_i == index_j:
                    # Trivial case
                    continue
                
                # Remove the char from i,j
                digits_i.remove(char_to_remove)
                digits_j.remove(char_to_remove)
                num, denom = digits_i[0], digits_j[0]
                
                
                if denom == 0:
                    # Can't divide by 0
                    continue
                
                # Check if fractions are the same
                if float(num) / denom == float(i) / j:
                    numerators.append(num)
                    denominators.append(denom)

    # Lambda to multiply all elements in a list together
    product_lambda = lambda x, y: x*y
    
    # Find product of numerators, denominators
    numerator = reduce(product_lambda, numerators)
    denominator = reduce(product_lambda, denominators)
    
    # Reduce numerator/denominator
    numerator, denominator = reduce_fraction(numerator, denominator)
    
    print('The reduced fraction is %d/%d'%(numerator, denominator))