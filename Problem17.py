"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

word_lookup = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100 : 'hundred',
    1000: 'thousand'
}

def number_to_string(number):
    original_number = number
    # Check for thousands
    quotient = number // 1000
    name = ''
    
    if quotient is not 0:
        name += '%s %s ' % (word_lookup[quotient], word_lookup[1000])
        number = number % 1000
    
    # Check for hundreds
    quotient = number // 100
    if quotient is not 0:
        name += '%s %s ' % (word_lookup[quotient], word_lookup[100])
        number = number % 100
    
    # Check for tens
    
    if number is not 0:
        quotient = number // 10
        
        # If the original number was over 100 we add and per British usage
        if original_number > 100:
            name += 'and '
        # Special case where 1-19
        if 1 <= number <= 19:
            name += '%s ' % word_lookup[number]
            number = 0
        else:
            name += '%s ' % word_lookup[quotient*10]
            number = number % 10
    
    # Check for ones
    if number is not 0:
        name += '%s ' % word_lookup[number]
    
    return name

if __name__ == "__main__":
    # Construct array of strings representing numbers from [1,1000] with white space removed.
    numbers = [number_to_string(a).replace(" ","") for a in xrange(1, 1001, 1)]
    
    # Join array by empty string
    number_str = ''.join(numbers)
    
    print 'The string length is %d characters' % len(number_str)