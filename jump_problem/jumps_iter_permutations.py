#########################################################
# Author: rawat s.
# Date: 2018-09-20
#########################################################

# solution 3: for those who love combinatorics
def jumps(n):
    fac = {0:1} # set fac[0] to 1 (0!)
    for i in range(1,n+1):
        # compute a table for factorials from 0! to n!
        fac[i] = i*fac[i-1]
    count = 0  # used to keep the total number of possible jumps
    (d4,d5) = (int(n/4), int(n/5))
    for i in range(0, d4+1): # try to select 4 (none, one or more)
        for j in range(0, d5+1): # try to select 5 (none, one or more)
            d = 4*i + 5*j # select one or more steps from {4,5}
            if d <= n: # if the sum of selected 4s and/or 5s less than n
                # number of digits (may be repeated)
                k = n - d + (i+j)
                # number of permutations with repeated 4s,5s
                m = fac[k] / ( fac[k-(i+j)]*fac[i]*fac[j] )
                count += m
    return int(count)

for i in range(1,51):
    print ( jumps(i) )

#########################################################
