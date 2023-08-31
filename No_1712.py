# 1712번) 손익분기점

from math import floor

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(floor(a/(c-b))+1)