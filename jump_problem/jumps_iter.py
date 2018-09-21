#########################################################
# Author: rawat s.
# Date: 2018-09-20
#########################################################

def jump(n):
    jump_list = [[0]]  # used to store lists of jumps
    jumps = []  # used to store strings representing all possible jump steps
    while jump_list:
        p = jump_list.pop()
        s = p[0]    # the first element is the sum of the following jump steps
        if s == n:  # finished (no more jumps)
            jumps.append(''.join([str(i) for i in p[1:]]))
        else:
            for i in [1, 4, 5]:
                if s + i <= n:
                    np = p + [i]  # crete a new list of jump steps
                    np[0] = s + i  # update the sum of jump steps
                    jump_list.insert(0, np)
    return jumps


# test code
for i in range(1, 10):
    sol = jump(i)
    print (i, '|', sol, '#', len(sol))
    for x in sol:
        print('sum', x, sum([int(i) for i in x]))
    print (10 * '-')

print (50 * '#')

#########################################################
