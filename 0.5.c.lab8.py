def det_c(n):
    d1 = 3
    d2 = 7
    for i in range(3, n+1):
        dn = 3*d2 - 2*d1
        d1 = d2
        d2 = dn
    return d2
n = 3
print(det_c(n))