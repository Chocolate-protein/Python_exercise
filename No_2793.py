# 2793번) 구구단

n = int(input())

for i in range(1, 10):
    print("{} * {} = {}".format(n, i, n*i))