"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

if __name__ == "__main__":
    numbers = []
    for i in xrange(1,1000000):
        from strings.patterns import is_palindrome
        
        # Convert decimal value to string
        decimal_string = str(i)
        
        # Check if its a palindrome
        if not is_palindrome(decimal_string):
            continue
        
        # Convert decimal value to binary string
        binary_string = "{0:b}".format(i)
        
        # Check if its a palindrome
        if is_palindrome(binary_string):
            numbers.append(i)
    
    print('The sum of all palindromic numbers in base 2 and base 10 is %d'%sum(numbers))
        