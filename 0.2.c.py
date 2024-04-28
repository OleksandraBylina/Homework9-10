n = 9 # how many numbers we need
x = 2 # our possible x
def seq_finder(n, x):
    k = 0
    xn_back = 1
    for i in range(n):
        k += 1
        bufer = k ** 2 - k + 1
        den = 1
        for i in range(2 * k):
            den = den * bufer
            bufer += 1
        xn = ((-x) / (den)) * xn_back
        xn_back = xn
        yield xn
for i in seq_finder(n, x):
    print(i)