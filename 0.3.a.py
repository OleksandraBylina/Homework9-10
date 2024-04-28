n = 50 # how many numbers we need # our possible x
def seq_finder(n):
    k = 1
    xn_back = 0.5
    sum = 0.5
    for i in range(n):
        k += 1
        xn = xn_back / (k + 1)
        sum += xn
        xn_back = xn
        yield sum
for i in seq_finder(n):
    print(i)