#########################################################
# Author: rawat s.
# Date: 2018-09-20
#########################################################

mem = []


def jump(n):
    global mem
    if n == 0:
        return []
    if mem[n]:
        # print ( 'use mem[{}]'.format(n) )
        return mem[n]
    p = []
    for i in [5, 4, 1]:
        if (n - i) >= 0:
            # print ( 'call jump({})'.format(n-i) )
            r = jump(n - i)  # return a complete list of possible jumps for (n-i)
            if not r:
                x = [i]
                p = p + [x]
            else:
                for e in r:
                    x = [] + e
                    x.insert(0, i)
                    p = p + [x]
    mem[n] = p
    # print ( 'set mem[{}] = {}'.format(n,p) )
    return p


# test code
N = 10
for i in range(1, N):
    mem = N * [[]]
    mem[1] = [[1]]
    mem[2] = [[1, 1]]
    mem[3] = [[1, 1, 1]]
    sol = jump(i)
    print ('{}) {} : {}'.format(i, len(sol), sol))

print (50 * '#')

print ('[Memory]')
for i in range(1, 10):
    print ('mem[{}] = {}'.format(i, mem[i]))

print (50 * '#')

#########################################################
