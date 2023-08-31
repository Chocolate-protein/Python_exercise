# 1997번) 완전제곱수

from math import *

m = int(input())
n = int(input())

num_list = list(range(m, n+1))
squa_list = list()

sum = 0

for i in num_list:
    if sqrt(i) == int(sqrt(i)):
        squa_list.append(i)
    

if squa_list == []:
    print(-1)
else:
    for i in squa_list:
        sum += i
    print(sum)
    print(min(squa_list))