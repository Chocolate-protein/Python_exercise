# 1408번) 24

now = input()
start = input()

def time(x):
    if x < 10:
        x = "0{}".format(x)
    return x

now = int(now[:2])*3600 + int(now[3:5])*60 + int(now[6:])
start = int(start[:2])*3600 + int(start[3:5])*60 + int(start[6:])

if now >= start:
    complete = (24*3600) - (now - start)
else:
    complete = start - now

h = complete//3600
m = (complete%3600)//60
s = (complete%3600)%60

print("{}:{}:{}".format(time(h), time(m), time(s)))