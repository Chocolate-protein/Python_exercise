# 1110번) 더하기 사이클

from math import *

n = int(input())
sum = 0
n_s = n
cycle = 0

while True:
    cycle += 1
    sum = floor(n/10) + n%10
    n = (n%10)*10 + sum%10
    if n == n_s:
        break
print(cycle)