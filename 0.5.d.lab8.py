def det_d(n):
    d1 = 0
    d2 = 1
    for i in range(3, n+1):
        dn = -d1
        d1 = d2
        d2 = dn
    return d2
print(det_d(n))