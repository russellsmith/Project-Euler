"""
In England the currency is made up of pound, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p) and 2 pound (200p).
It is possible to make 2 pounds in the following way:

1x1 pound + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 2 pounds be made using any number of coins?
"""
def generate_table(coins, target):
    table = []
    table_increments = 1
    # init table to all 0s
    for i in xrange(0,target / table_increments + 1):
        table.append([0]*len(coins))
        
    # Each row in table represents multiples of 5 pence
    # Each column represents # of coins used
    # i.e. column 1 represents ways to generate money using
    # only 1p
    # column 2 represents ways to generate money using 1p or 2p
    for n in xrange(0, len(table)):
        # working with coin values with multiple of 5
        target_value = n * table_increments
        for k in xrange(len(coins)):
            coin_value = coins[k]
            
            # Target value is 0, or only using 1p coins if k == 0
            # in both cases the value can only be reached one way
            if n == 0 or k == 0:
                table[n][k] = 1
                continue
            
            prev_k = k - 1
            prev_value = (target_value - coin_value)/table_increments
            
            dont_use_coin_c = table[n][prev_k]
            
            if prev_value < 0:
                do_use_coin_c = 0
            else:
                do_use_coin_c = table[prev_value][k]
                
            num_combinations = dont_use_coin_c + do_use_coin_c
            table[n][k] = num_combinations
    return table
    

if __name__ == "__main__":
    coins = [1,2, 5,10,20,50,100,200]
    target = 200
    table = generate_table(coins, target)
    rows = len(table)
    print('The number of ways to reach %d with %s is %d'%(target, coins, table[rows - 1][len(coins) - 1]))