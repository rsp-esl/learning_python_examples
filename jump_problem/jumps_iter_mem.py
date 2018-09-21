#########################################################
# Author: rawat s.
# Date: 2018-09-20
#########################################################

def jump(n):
    mem = {0: [[]]}
    for i in range(1, n + 1):
        p = []
        for j in [1, 4, 5]:
            if i >= j:
                m = mem[i - j]
                for e in m:
                    p += [e + [j]]
        mem[i] = p
    return mem


results = jump(9)

for i in range(1, len(results)):
    print(i, len(results[i]), results[i])

#########################################################
