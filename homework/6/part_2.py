q = [['a','b','c'],['d','e','f'],['g','h']]
for n in range(0,len(q)):
    for k in range(0,len(q[n])):
        m = q[n]
        print(m[k],end="")
        k += 1
    n += 1
print()