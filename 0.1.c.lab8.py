import math
n = int(input())
def seq_finder(n):
    a0 = 1
    a1 = 1
    k = 3
    sum = 0
    for i in range(n):
        ak = (a0 / (2 ** k)) + a1
        a1 = ak
        a0 = a1
        k = k + 1
        sum += (math.factorial(k)) / ak
        yield sum
for i in seq_finder(n):
    print(i)
