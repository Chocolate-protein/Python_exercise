# 2869번) 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())

if (v-b) % (a-b) == 0:  
    x = (v-b) // (a-b)
    print(x)
else:
    x = ((v-b) // (a-b)) + 1
    print(x)

'''
import sys
import math
a, b, v = map(int, input().split())
day = (v-b) / (a-b)
print(math.ceil(day))
'''