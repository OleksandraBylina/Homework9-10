x = (2)
a0 = x
eps = 0.000001
n = 1
back_summ = x

while True:
    an = (16 + x) / (1 + abs(a0 ** 3))
    summ = back_summ + an
    #print (summ)
    if abs(summ - back_summ) <= eps:
        print(summ)
        break
    back_summ = summ
    a0 = an
    n = n + 1