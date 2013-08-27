"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def num_digits(number):
    return len(str(number))
    

if __name__ == "__main__":
    from maths.sequences import fibonacci
    digit_limit = 1000
    
    for f, iteration in fibonacci():
        if num_digits(f)>= digit_limit:
            result = f
            break
    
    print 'The %dth fibonacci number %d was over 1000 digits' %(iteration, result)
        