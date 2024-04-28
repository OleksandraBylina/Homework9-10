x = (1)
a0 = 1
eps = 0.0000001
n = 1
back_summ = 1

while True:
    an = (((x ** 2) ) / (2 * (n + 1))) * a0
    summ = back_summ + an
    #print (summ)
    if abs(summ - back_summ) <= eps:
        print(summ)
        print (n)
        break
    back_summ = summ
    a0 = an
    n = n + 1