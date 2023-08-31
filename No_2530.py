#  2530번) 인공지능 시계

from math import *

h, m, s = map(int, input().split())
cook = int(input())

cook_h = floor(cook/3600)
cook -= cook_h * 3600

cook_m = floor(cook/60)
cook -= cook_m * 60

cook_s = floor(cook)

h += cook_h
m += cook_m
s += cook_s

while s >= 60:
        s -= 60
        m += 1

while m >= 60:
        m -= 60
        h += 1

while h >= 24:
        h -= 24

print("{} {} {}".format(h, m, s))