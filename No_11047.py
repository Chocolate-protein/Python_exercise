# 11047번) 동전

import sys

n, k = map(int, sys.stdin.readline().split())
coin = list()

for _ in range(0, n):
    coin.append(int(sys.stdin.readline()))

coin.sort(reverse= True)
count = 0

for i in coin:
    count += k//i
    k = k%i

print(count)