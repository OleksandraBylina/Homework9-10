n = int(input())
def seq_finder(n):
    a0 = 1
    a1 = 1
    k = 3
    sum = 0
    for i in range(n):
        ak = (a1 / k) + a0
        a1 = ak
        a0 = a1
        k = k + 1
        sum += (3 ** k) / (ak)
        yield sum
for i in seq_finder(n):
    print(i)
