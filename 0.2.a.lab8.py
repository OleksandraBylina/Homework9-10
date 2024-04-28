import math
x = (0.5)
a0 = x
eps = 0.00000000000000000001
n = 2
back_summ = x

while True:
    an = ((x ** 2) / (((2 * n) - 1) * ((2 * n) - 2))) * a0
    summ = back_summ + an
    #print (summ)
    if summ - back_summ <= eps:
        print(summ)
        break
    back_summ = summ
    a0 = an
    n = n + 1
print (math.sinh(0.5))