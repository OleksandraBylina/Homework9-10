n = int(input())
def seq_finder(n):
    a0 = 0
    a1 = 1
    b0 = 1
    b1 = 1 # unnecessary info
    k = 3
    sum = 0
    for i in range(n):
        bk = b0 + a1
        ak = (a1 / k) + (a0 * bk)
        b0 = bk
        a1 = ak
        a0 = a1
        k = k + 1
        sum += (2 ** k) / (ak + bk)
        yield sum
for i in seq_finder(n):
    print(i)
