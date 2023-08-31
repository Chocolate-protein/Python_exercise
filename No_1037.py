# 1037번) 약수

from math import *

def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
num_list = list(map(int, input().split()))

if len(num_list) == 1 and prime(num_list[0]) == True:
    ans = int(pow(num_list[0], 2))

else:
    ans = num_list[0]
    for i in range(1, len(num_list)):
        ans = lcm(ans, num_list[i])
    if ans == max(num_list):
        ans *= min(num_list)

print(ans)