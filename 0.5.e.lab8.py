def det_e(n, a):
    d1 = a
    d2 = a**2 - 1
    for i in range(3, n+1):
        dn = d2*a - d1
        d1 = d2
        d2 = dn
    return d2
print(det_e(n))