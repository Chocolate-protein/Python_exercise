# 10773번) 제로

import sys

k = int(sys.stdin.readline())
result = list()

for i in range(0, k):
    n = int(sys.stdin.readline())
    if n == 0:
        result.pop()
    else:
        result.append(n)

print(sum(result))
