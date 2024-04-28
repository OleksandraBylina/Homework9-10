k = int(input())
def seq_finder(k):
    n = 0
    an_back = 0
    #an = 0
    for i in range(k):
        an = (an_back + 2) ** 0.5
        yield an
        n += 1
        an_back = an
for i in seq_finder(k):
    print(i)
