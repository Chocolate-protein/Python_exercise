# 1676번) 팩도리얼 0의 개수

import math
import sys

n = int(sys.stdin.readline())
num = list(str(math.factorial(n)))
num.reverse()

for i in num:
    if i != "0":
        print(num.index(i))
        break
