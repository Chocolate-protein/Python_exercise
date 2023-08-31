# 2884번) 알람 시계

h, m = map(int, input().split())

m = m - 45

if m < 0:
    h -= 1
    m = 60 + m
elif m >= 60:
    h += 1
    m = m - 60

if h >= 24:
    h -= 24
elif h < 0:
    h += 24

print("{} {}".format(h, m))