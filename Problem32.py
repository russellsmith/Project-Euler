"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def get_unique_digits(number):
    digits = set()
    all_unique = True
    while number > 0:
        digit = number % 10
        if digit not in digits:
            digits.add(digit)
        else:
            all_unique = False
        number = number / 10
        
    return digits, all_unique

if __name__ == "__main__":
    # target_sum = sum of digits 1-9
    target_sum = sum(xrange(10))
    multipliers = set()
    products = set()
    for i in xrange(10000):
        for j in xrange(1000):
            if i in multipliers and j in multipliers:
                continue
            i_digits, i_unique = get_unique_digits(i)
            if not i_unique:
                continue
            j_digits, j_unique = get_unique_digits(j)
            
            intersection = j_digits.intersection(i_digits)
            if not j_unique or len(intersection) is not 0:
                continue
            
            union_digits = j_digits.union(i_digits)
            product = i * j
            p_digits, p_unique = get_unique_digits(product)
            intersection = p_digits.intersection(union_digits)
            if not p_unique or len(intersection) is not 0:
                continue
            
            # Check that we have all 9 digit values
            union_digits |= p_digits
            if len(union_digits) is not 9:
                continue
            
            # Check that the sum of digits is the target_sum
            if sum(union_digits) is target_sum:
                multipliers.add(i)
                multipliers.add(j)
                products.add(product)
    print('The sum of pandigital products is %d'%sum(products))
            