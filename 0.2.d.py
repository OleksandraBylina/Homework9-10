n = 10 # how many numbers we need
x = 2 # our possible x
def seq_finder(n, x):
    k = 0
    xn_back = 1
    for i in range(n):
        k += 1
        xn = ((x**2) / ((4*(k**2)) - (2 * k))) * xn_back
        xn_back = xn
        yield xn
for i in seq_finder(n, x):
    print(i)