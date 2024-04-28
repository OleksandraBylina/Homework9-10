import math
x = (0.5)
a0 = 1
eps = 0.0000000000000001
n = 2
back_summ = 1

while True:
    an = (((-x) * n) / (n - 1)) * a0
    summ = back_summ + an
    #print (summ)
    if abs(summ - back_summ) <= eps:
        print(summ)
        break
    back_summ = summ
    a0 = an
    n = n + 1
print (1 / ((1 + x) ** 2))