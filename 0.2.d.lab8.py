import math
x = (0.5)
a0 = x 
eps = 0.00000000001
n = 2
back_summ = x * 2

while True:
    an = ((x ** 2) * (((2 * n) - 3)) /   ((2 * n) - 1)) * a0
    summ = ((back_summ + (an * 2)))
    #print (summ)
    if abs(summ - back_summ) <= eps:
        print(summ)
        break
    back_summ = summ
    a0 = an
    n = n + 1
print (math.log((1 + x) / (1 - x)))