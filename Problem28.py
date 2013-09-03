"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def generate_spiral(dimension):
    spiral = []
    offset = 1
    count = 1
    total = dimension * dimension
    half = dimension/2
    x,y = half, half
    
    for i in xrange(dimension):
        spiral.append([0]*dimension)
    
        
    while True:
        while x < half + offset:
            # Move right up to offset
            spiral[y][x] = count
            x += 1
            count += 1
            
        if count >= total:
            break
        
        while y < half + offset:
            # Move down up to offset
            spiral[y][x] = count
            y += 1
            count += 1
        
        while x > half - offset:
            # Move left up to offset
            spiral[y][x] = count
            x -= 1
            count += 1
        
        while y > half - offset:
            spiral[y][x] = count
            y -= 1
            count += 1
            
        offset += 1
        
    return spiral

def sum_diagonals(matrix):
    dimension = len(matrix)
    sum = 0
    
    for i in xrange(dimension):
        # find indexes of both elements to pull from the row
        a, b = i , dimension - (i + 1)
        
        if a != b:
            sum += matrix[i][a] + matrix[i][b]
        else:
            sum += matrix[i][a]
            
    return sum
        
    
    
if __name__ == "__main__":
    dimension = 1001
    spiral = generate_spiral(dimension)
    
    sum = sum_diagonals(spiral)
    
    print('The sum of diagonals of dimension %d is %d'%(dimension, sum))
    
    