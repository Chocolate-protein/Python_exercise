# 2525번) 오븐 시계

from math import *

h, m = map(int, input().split())
cook = int(input())

cook_h = floor(cook/60)
cook_m = floor(cook%60)

h += cook_h
m += cook_m

if m >= 60:
    m -= 60
    h += 1

if h >= 24:
    h -= 24

print("{} {}".format(h, m))