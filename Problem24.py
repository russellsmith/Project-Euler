"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
if __name__ == "__main__":
    from maths.misc import generate_permutations
    
    nums = "0123456789"
    perms = []
    for i in generate_permutations(nums):
        perms.append(i)
    perms = [int(perm) for perm in perms]
    perms.sort()
    
    
    print 'The millionth item is %d' % perms[999999]