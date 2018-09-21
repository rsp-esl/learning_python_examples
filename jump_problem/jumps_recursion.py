#########################################################
# Author: rawat s.
# Date: 2018-09-20
#########################################################


def jump(n, s=[]):
    if n == 0:  # base case
        return [s]
    p = []
    for i in [1, 4, 5]:
        if n >= i:
            p += jump(n - i, s + [i])
    return p


# test code
for i in range(1, 10):
    sol = jump(i, [])
    print (i, len(sol), sol )
    for x in sol:
        print ('sum', sum([int(i) for i in x]), x)
    print (10 * '-')

print (50 * '#')

#########################################################
