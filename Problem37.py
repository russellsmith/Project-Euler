"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def remove_digits(number):
    from maths.misc import get_digits, digit_list_to_num
    digits = get_digits(number)
    num_digits = len(digits)
    
    for i in xrange(1, num_digits):
        # Remove digits from the right
        yield digit_list_to_num(digits[:i])
        
        # Remove digits from the left
        yield digit_list_to_num(digits[i:])
    

if __name__ == "__main__":
    matching_primes = []
    from maths.misc import is_prime
    from maths.sequences import prime_numbers
    
    exclusion_set = (2, 3, 5, 7)
    # Start prime search at 10
    for prime_number in prime_numbers(limit = None, start = 10):
        if len(matching_primes) > 10:
            break
        found_prime = True
        for n in remove_digits(prime_number):
            if n is 1 or not is_prime(n):
                found_prime = False
                break
        
        if found_prime:
            matching_primes.append(prime_number)
    print('Matching primes: %s'%matching_primes)
    print('The sum of matching primes is %d'%sum(matching_primes))
    