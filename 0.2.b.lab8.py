import math
x = (0.5)
a0 = x
eps = 0.0000000000000001
n = 2
back_summ = x

while True:
    an = (-((x * (n-1)) / n) * a0)
    summ = back_summ + an
    #print (summ)
    if abs(summ - back_summ) <= eps:
        print(summ)
        break
    back_summ = summ
    a0 = an
    n = n + 1
print (math.log(1 + x))