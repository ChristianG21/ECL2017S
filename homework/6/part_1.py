Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
n = 0
print('    C     F')
while n < len(Cdegrees):
    F = (9.0/5)*Cdegrees[n] + 32
    print('%5d %5.1f' % (Cdegrees[n],F))
    n += 1